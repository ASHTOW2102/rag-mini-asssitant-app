from PyPDF2 import PdfReader
import os

def extract(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return "\n".join([p.extract_text() for p in reader.pages if p.extract_text()])
    except Exception as e:
        print(f"Skipping {pdf_path}, reason: {e}")
        return ""

def chunk(text, size=300):
    return [text[i:i+size] for i in range(0, len(text), size)]

if __name__ == "__main__":
    docs_dir = "../data"
    all_chunks = []
    for filename in os.listdir(docs_dir):
        if filename.endswith(".pdf"):
            text = extract(os.path.join(docs_dir, filename))
            if text:
                chunks = chunk(text)
                all_chunks.extend(chunks)
    with open("chunks.txt", "w") as f:
        for c in all_chunks:
            f.write(c.replace("\n", " ") + "\n")
