from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_embeddings(chunks):
    return model.encode(chunks)

if __name__ == "__main__":
    with open("chunks.txt", "r") as f:
        chunks = [line.strip() for line in f if line.strip()]
    embeddings = compute_embeddings(chunks)
    # Save embeddings and chunks for faiss_store
    import numpy as np
    np.save("embeddings.npy", embeddings)
    with open("chunks_proc.txt", "w") as f:
        for c in chunks:
            f.write(c + "\n")
