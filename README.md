# 🤖 RAG Mini Assistant

A **Retrieval-Augmented Generation (RAG) Mini Assistant** built with **Gradio, FAISS, and OpenAI GPT**, designed to answer questions using pre-processed context stored in embeddings.

---

## 🚀 Live Demo

👉 [Hugging Face Space](https://huggingface.co/spaces/AshishChaturvedi7/rag-mini-assistant-app)

---

## 🚀 Features

- Uses **Sentence Transformers** (`all-MiniLM-L6-v2`) to encode queries.
- Retrieves top-matching context with **FAISS** vector search.
- Generates answers with **OpenAI GPT** using retrieved knowledge.
- Interactive **Gradio UI** with a clean, modern theme.
- Deployable locally or on **Hugging Face Spaces**.

---

## 📂 Project Structure

```

├── data/ # Folder containing raw documents
├── chunk_doc.py # Script to split documents into chunks
├── embedding.py # Script to create embeddings + FAISS index
├── faiss_store.py # Script to save/load FAISS index
├── main.py # RAG assistant app with Gradio UI
├── requirements.txt # Dependencies
└── README.md # Documentation

```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ASHTOW2102/rag-mini-asssitant-app.git
   cd rag-mini-asssitant-app
   ```
