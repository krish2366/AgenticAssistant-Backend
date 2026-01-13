from fastapi import FastAPI
from app.api.ask import router as ask_router
from app.api.ingest import router as ingest_router
from app.api.projects import router as projects_router

app = FastAPI(
    title="Agentic Codebase Assistant",
    version="1.0.0"
)

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(ask_router, prefix="/ask", tags=["Ask"])
app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(projects_router, prefix="/projects", tags=["Projects"])