from supabase import create_client 
from app.config import SUPABASE_KEY, SUPABASE_URL
from app.ingestion.embedder import embed_text

supabase = create_client(SUPABASE_URL,SUPABASE_KEY)

def retrieve(project_id: str, question: str, top_k: int = 5):
    if not project_id:
        raise ValueError("retrieve: project_id is required")

    if not question or not question.strip():
        raise ValueError("retrieve: question must be non-empty")

    if top_k <= 0:
        raise ValueError("retrieve: top_k must be > 0")
    
    query_embedding = embed_text(question)
    
    response = supabase.rpc(
        "match_code_chunks", {
            "query_embedding": query_embedding,
            "match_count": top_k,
            "project_id": project_id
        }
    ).execute()


    return response.data