from supabase import create_client 
from app.config import SUPABASE_KEY, SUPABASE_URL

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_chunk(data: dict):
    try:
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if not data:
            raise ValueError("data cannot be empty")

        supabase.table("code_chunks").insert(data).execute()

    except Exception as e:
        print(f"[store_chunk error] {e}")
