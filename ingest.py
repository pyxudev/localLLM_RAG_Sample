import os
from tqdm import tqdm

# Refer: https://qiita.com/shiozaki/items/63447ec6617ded9840b3
# "Pydantic V1 functionality" という文字列を含む UserWarning を無視する
# メッセージ内容でフィルタリングすることで、どのモジュール経由の発生でも捕捉可能です
import warnings
warnings.filterwarnings("ignore", message=".*Pydantic V1 functionality.*")

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters  import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

PDF_DIR = "./pdf"
MD_DIR = "./md"
DB_DIR = "./db"

# embedding
embeddings = OllamaEmbeddings(model="nomic-embed-text")

all_docs = []
pdfs = []
mds = []

print("Loading documents...")

# PDF読み込み
for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        path = os.path.join(PDF_DIR, file)
        loader = PyPDFLoader(path)
        pdfs.extend(loader.load())

print(f"Loaded PDF all_docs: {len(pdfs)}")
all_docs.extend(pdfs)

# Markdown読み込み
for file in os.listdir(MD_DIR):
    if file.endswith(".md"):
        path = os.path.join(MD_DIR, file)
        loader = TextLoader(
            path,
            encoding="utf-8"
        )
        mds.extend(loader.load())

print(f"Loaded Markdown all_docs: {len(mds)}")
all_docs.extend(mds)

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
