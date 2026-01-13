from app.rag.retrieval import retrieve 
from app.agents.state import AgentState

def search_file_node(state: AgentState) -> dict:
    results = retrieve(
        project_id= state["project_id"],
        question=state["question"]
    )
    
    chunks = [r["content"] for r in results]
    
    return {
        "tool_name": "search_file",
        "tool_input": state["question"],
        "tool_result": '\n\n'.join(chunks),
        "retrieved_chunks": chunks,
        "reasoning": state["reasoning"] + [
            f"search_file used with question: {state['question']}"
        ],
    }
    
    