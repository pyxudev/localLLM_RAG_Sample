import os
from tqdm import tqdm

# Refer: https://qiita.com/shiozaki/items/63447ec6617ded9840b3
# "Pydantic V1 functionality" という文字列を含む UserWarning を無視する
# メッセージ内容でフィルタリングすることで、どのモジュール経由の発生でも捕捉可能です
import warnings
warnings.filterwarnings("ignore", message=".*Pydantic V1 functionality.*")

from langchain_community.document_loaders import (
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader
)
from langchain_chroma import Chroma
from langchain_text_splitters  import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

DOCX_DIR = "./docx"
PDF_DIR = "./pdf"
MD_DIR = "./md"
DB_DIR = "./db"

# embedding
print("Start embedding")
embeddings = OllamaEmbeddings(model="nomic-embed-text")
loaders = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
    ".md": TextLoader
}
all_docs = []

print("Loading documents...")
for dir_path_list in [[PDF_DIR, "PDF"], [DOCX_DIR, "DOCX"], [MD_DIR, "MD"]]:
    temp_list = []
    for file in os.listdir(dir_path_list[0]):
        ext = os.path.splitext(file)[1]
        if ext in loaders:
            path = os.path.join(dir_path_list[0], file)
            loader = loaders[ext](path)
            temp_list.extend(loader.load())
    print(f"Loaded {dir_path_list[1]} files: {len(temp_list)}")
    all_docs.extend(temp_list)

# チャンク分割
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=80,
)

splits = splitter.split_documents(all_docs)
print(f"Split chunks: {len(splits)}")

# VectorDB保存
vectordb = Chroma(
    embedding_function=embeddings,
    persist_directory=DB_DIR,
)

batch_size = 20
texts = [doc.page_content for doc in splits]

for i in tqdm(range(0, len(splits), batch_size), desc="Embedding"):
    batch = splits[i:i + batch_size]
    vectordb.add_documents(batch)

print("Done. Vector DB saved.")
