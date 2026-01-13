from fastapi import APIRouter, HTTPException
from app.api.schema import ProjectsResponse
from app.services.project_service import project_service


router = APIRouter()

@router.get("", response_model= ProjectsResponse)
def list_projects():
    try:
        projects = project_service.list_projects()
        return {
            "projects" : projects
        }
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail= "failed to fetch projects"
        )