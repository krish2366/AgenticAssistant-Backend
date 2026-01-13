# embedding chunking to vector of size 348

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if not text.strip():
            raise ValueError("text cannot be empty")

        embedding = model.encode(text, normalize_embeddings=True)
        return embedding.tolist()

    except Exception as e:
        print(f"[embed_text error] {e}")
        return []
