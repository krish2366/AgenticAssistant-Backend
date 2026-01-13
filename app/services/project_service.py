from supabase import create_client 
from app.config import SUPABASE_KEY, SUPABASE_URL

client = create_client(SUPABASE_URL,SUPABASE_KEY)

class ProjectService:
    def list_projects(self):
        response = (
            client
            .table("projects")
            .select("project_id","project_name")
            .order("created_at", desc= True)
            .execute()
        )
        
        return response.data or []
    
project_service = ProjectService()