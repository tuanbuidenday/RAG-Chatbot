from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Load PDF
loader = PyPDFLoader("data/documents/Dieu-le-cong-ty.pdf")
documents = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Embedding
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Load or Create
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("data/vectorstore")