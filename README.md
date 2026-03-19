# RAG-Chatbot

🧠 RAG Chatbot (FastAPI + Streamlit + Ollama)

A Retrieval-Augmented Generation (RAG) chatbot built with:
• ⚡ FastAPI (Backend API)
• 🎨 Streamlit (UI)
• 🧠 Ollama (LLM + Embeddings)
• 🔍 FAISS (Vector Database)
• 🐳 Docker & Docker Compose

▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open:

```bash
http://127.0.0.1:8000/docs
```

🎨 Run Streamlit

```bash
streamlit run app/app.py
```

Open:

```bash
http://localhost:8501
```

🐳 Run with Docker

```bash
docker compose up --build
```
