from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=OLLAMA_BASE_URL)

# check folder
if not os.path.exists("data/vectorstore"):
    raise ValueError("Chưa có vectorstore, cần tạo trước!")

vectorstore = FAISS.load_local(
    "data/vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5, "fetch_k": 10}
)
llm = ChatOllama(model="llama3", base_url=OLLAMA_BASE_URL)

def ask(question):
    docs = retriever.invoke(question)
    print("Question:", question)
    print("Docs found:", len(docs))
    for i, d in enumerate(docs[:3]):
        print(f"--- DOC {i+1} ---")
        print(d.page_content[:500])
        print(d.metadata)
    if not docs:
        return "Không tìm thấy thông tin liên quan"
    context = "\n".join([d.page_content for d in docs])
    prompt = f"""
Bạn là trợ lý AI. Chỉ trả lời dựa trên context.
Nếu không có thông tin, nói "Tôi không biết".

Context:
{context}

Question: {question}
"""

    return llm.invoke(prompt).content