from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = FAISS.load_local(
    "data/vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)
# Retriever
retriever = vectorstore.as_retriever()

# LLM
llm = ChatOllama(model="llama3")

def ask(question):
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Câu trả lời dựa trên ngữ cảnh sau:

{context}

Question: {question}
"""
    return llm.invoke(prompt).content