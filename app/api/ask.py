from fastapi import APIRouter, HTTPException 
from app.services.agent_service import agent_service
from app.api.schema import AskRequest,AskResponse

router = APIRouter()

@router.post("",response_model= AskResponse)
def ask_question(payload: AskRequest):
    try:
        result = agent_service.ask(
            project_id= payload.project_id,
            question= payload.question
        )
        return result
        
    except ValueError as e:
        raise HTTPException(status_code= 404, detail=str(e))
        
    except Exception as e:
        print("[LOGGER]",str(e))
        raise HTTPException(
            status_code=500,
            detail="Agent failed to process the request"
        )
        