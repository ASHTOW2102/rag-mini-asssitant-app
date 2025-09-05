import gradio as gr
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chunks = [line.strip() for line in open("chunks_proc.txt", encoding="utf-8")]
embeddings = np.load("embeddings.npy")
index = faiss.read_index("faiss_index.bin")
model = SentenceTransformer('all-MiniLM-L6-v2')

def ask_gradio(question):
    q_emb = model.encode([question])
    _, I = index.search(np.array(q_emb).astype(np.float32), k=3)
    context = " ".join(chunks[i] for i in I[0])
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message.content
    return answer

with gr.Blocks(theme=gr.themes.Soft(), css="""
    body {background: rgba(173, 216, 230, 0.3);}
    .gradio-container {max-width: 700px; margin: auto;}
    .output-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 15px;
        border-radius: 15px;
        color: white;
        font-size: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
        white-space: pre-wrap;
    }
""") as demo:

    gr.Markdown(
        "<h1 style='text-align:center;color:white;'>🤖 RAG Mini Assistant</h1>"
        "<p style='text-align:center;color:white;'>Enter your question below to get answers based on indexed context.</p>"
    )

    with gr.Row():
        question_input = gr.Textbox(label="Enter your question", placeholder="Ask anything...")

    generate_btn = gr.Button("Get Answer")
    output_box = gr.Markdown(elem_classes="output-card")

    generate_btn.click(fn=ask_gradio, inputs=question_input, outputs=output_box)


if __name__ == "__main__":
    demo.launch(share=True)
