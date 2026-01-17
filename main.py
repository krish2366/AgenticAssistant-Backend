from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.ask import router as ask_router
from app.api.ingest import router as ingest_router
from app.api.projects import router as projects_router

app = FastAPI(
    title="Agentic Codebase Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(ask_router, prefix="/ask", tags=["Ask"])
app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(projects_router, prefix="/projects", tags=["Projects"])