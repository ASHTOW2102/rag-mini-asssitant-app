from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import openai
import os
from dotenv import load_dotenv


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


chunks = [line.strip() for line in open("chunks_proc.txt", encoding="utf-8")]
embeddings = np.load("embeddings.npy")
index = faiss.read_index("faiss_index.bin")
model = SentenceTransformer('all-MiniLM-L6-v2')  


class AskRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request: AskRequest):
    query = request.question
    q_emb = model.encode([query])
    _, I = index.search(np.array(q_emb).astype(np.float32), k=3)
    context = " ".join(chunks[i] for i in I[0])

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": query}
        ]
    )

    answer = response.choices[0].message.content
    return {"answer": answer}
