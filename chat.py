from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from prompt_toolkit import prompt

DB_DIR = "./db"

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectordb = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings,
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

llm = OllamaLLM(model="tinyllama")

print("RAG Chat ready. Ctrl+C or /quit or /exit or /q to exit")

while True:
    question = prompt("\n> ")

    if question.lower() in ["/quit", "/exit", "/q"]:
        print("Exiting...")
        break

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    q_prompt = f"""
Please answer the question ONLY related to following information:

{context}

Question: {question}
"""
    print("\nAnalyzing...")

    res = llm.invoke(q_prompt)
    print("\n=========Answer Start=========\n", res)
    print("\n=========Answer End=========\n")

exit(0)
