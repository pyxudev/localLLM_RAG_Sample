from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

DB_DIR = "./db"

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectordb = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings,
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

llm = OllamaLLM(model="tinyllama")

print("RAG Chat ready. Ctrl+C to exit")

while True:
    question = input("\nQ: ")

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Please answer the question ONLY related to following information:

{context}

Question: {question}
"""

    res = llm.invoke(prompt)
    print("\nA:", res)