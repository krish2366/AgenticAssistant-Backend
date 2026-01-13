import os
import uuid

from supabase import create_client
from app.config import SUPABASE_KEY, SUPABASE_URL

from app.ingestion.chunker import chunk_text, extract_metadata
from app.ingestion.embedder import embed_text
from app.ingestion.store import store_chunk
from app.ingestion.loader import load_files

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class IngestionService:
    def ingest_repo(self, project_name: str, repo_path: str) -> dict:
        if not os.path.isdir(repo_path):
            raise ValueError("Invalid Repo path")
        
        project_id = str(uuid.uuid4())
        
        files = load_files(repo_path)
        files_processed = len(files)
        
        supabase.table("projects").insert({
            "project_id": project_id,
            "project_name": project_name
        }).execute()
        
        for file in files:
            chunks = chunk_text(file["content"])
            language, module = extract_metadata(file["file_path"])

            for chunk in chunks:
                embedding = embed_text(chunk)
                
                store_chunk({
                    "project_id": project_id,
                    "file_path" : file["file_path"],
                    "language" : language,
                    "module" : module,
                    "content" : chunk,
                    "embedding" : embedding
                })
        
        return {
            "project_id": project_id,
            "project_name": project_name,
            "status": "ingested",
            "files_processed": files_processed 
        }
            
ingestion_service = IngestionService()   