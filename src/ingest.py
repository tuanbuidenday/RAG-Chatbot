from turtle import st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Load PDF
docs_path = "data/documents"
all_docs = []

for file in os.listdir(docs_path):
    if file.endswith(".pdf"):
        file_path = os.path.join(docs_path, file)
        loader = PyPDFLoader(file_path)
        all_docs.extend(loader.load())
# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(all_docs)
print(chunks[0].page_content)
print(chunks[1].page_content)

# Embedding
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=OLLAMA_BASE_URL)

# Load or Create
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("data/vectorstore")