from app.rag.retrieval import retrieve
from app.agents.state import AgentState


def retrieve_node(state: AgentState) -> dict:
    results = retrieve(
        project_id= state["project_id"],
        question= state["question"]
    )
    
    chunks = [r["content"] for r in results]
    
    return {
        "retrieved_chunks": chunks
    }