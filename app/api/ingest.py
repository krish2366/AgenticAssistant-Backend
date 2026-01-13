from fastapi import APIRouter, HTTPException 
from app.api.schema import IngestRequest, IngestResponse
from app.services.ingestion_service import ingestion_service
 
router = APIRouter()

@router.post("", response_model= IngestResponse)
def ingest_repo(payload: IngestRequest):
    try:
        result = ingestion_service.ingest_repo(
            project_name= payload.project_name,
            repo_path= payload.repo_path
        )
        
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        print(e)
        
        raise HTTPException(
            status_code=500,
            detail="Failed to ingest repository"
        )