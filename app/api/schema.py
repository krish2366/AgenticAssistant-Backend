from pydantic import BaseModel, Field 
from typing import List, Optional

class AskRequest(BaseModel):
    project_id: str = Field(..., description="project id of ingested repo")
    question: str = Field(..., min_length=1, description="User question about the codebase")

    
class AskResponse(BaseModel):
    answer: str
    tool_used: Optional[str]
    reasoning: List[str]
    
    
class Project(BaseModel):
    project_id: str
    project_name: str


class ProjectsResponse(BaseModel):
    projects: List[Project]
    
    
    
class IngestRequest(BaseModel):
    project_name: str = Field(..., min_length= 1)
    repo_path: str = Field(..., description="Local path to the code repository")
    
class IngestResponse(BaseModel):
    project_id: str
    project_name: str
    status: str
    files_processed: int
    