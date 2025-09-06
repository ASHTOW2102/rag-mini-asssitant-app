# 🤖 RAG Mini Assistant

A **Retrieval-Augmented Generation (RAG) Mini Assistant** built with **Gradio, FAISS, and OpenAI GPT**, designed to answer questions using pre-processed context stored in embeddings.

---

## 🚀 Features

- Uses **Sentence Transformers** (`all-MiniLM-L6-v2`) to encode queries.
- Retrieves top-matching context with **FAISS** vector search.
- Generates answers with **OpenAI GPT** using retrieved knowledge.
- Interactive **Gradio UI** with a clean, modern theme.
- Deployable locally or on **Hugging Face Spaces**.

---

## 📂 Project Structure

```markdown
```

├── data/                 # Folder containing raw documents
├── chunk\_doc.py          # Script to split documents into chunks
├── embedding.py          # Script to create embeddings + FAISS index
├── main.py               # RAG assistant app with Gradio UI
├── requirements.txt      # Dependencies
└── README.md             # Documentation

```
```


---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ASHTOW2102/rag-mini-asssitant-app.git
   cd rag-mini-asssitant-app
   ```
