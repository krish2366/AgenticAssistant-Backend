import uuid 
from app.ingestion.loader import load_files
from app.ingestion.embedder import embed_text
from app.ingestion.chunker import chunk_text, extract_metadata
from app.ingestion.store import store_chunk

REPO_PATH = "./sample_repo2"

project_id = str(uuid.uuid4())
print("project id: ", project_id)

files = load_files(REPO_PATH)

for file in files:
    chunks = chunk_text(file["content"])
    language, module = extract_metadata(file["file_path"])
    
    for chunk in chunks:
        embedding = embed_text(chunk)
        
        store_chunk({
            "project_id": project_id,
            "file_path": file["file_path"],
            "language": language,
            "module": module,
            "content": chunk,
            "embedding": embedding
        })

print("ingestion completed")