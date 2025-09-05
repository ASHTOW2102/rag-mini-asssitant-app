import numpy as np
import faiss

embeddings = np.load("embeddings.npy")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "faiss_index.bin")
