# breaking content into chunks

import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, chunk_size=400, overlap=50):
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")

        if overlap < 0 or overlap >= chunk_size:
            raise ValueError("overlap must be >= 0 and < chunk_size")

        tokens = enc.encode(text)
        chunks = []

        start = 0

        while start < len(tokens):
            end = start + chunk_size
            chunk_token = tokens[start:end]
            chunk_text = enc.decode(chunk_token)
            chunks.append(chunk_text)

            start += chunk_size - overlap

        return chunks

    except Exception as e:
        print(f"[chunk_text error] {e}")
        return []


def extract_metadata(file_path: str):
    try:
        if not isinstance(file_path, str):
            raise TypeError("file_path must be a string")

        if not file_path:
            raise ValueError("file_path cannot be empty")

        parts = file_path.split("/")
        language = file_path.split(".")[-1]
        module = "/".join(parts[:-1])

        return language, module

    except Exception as e:
        print(f"[extract_metadata error] {e}")
        return None, None
