from app.agents.state import AgentState

def respond_node(state: AgentState) -> dict:

    return {
        "answer": state["answer"],
        "tool_name": state.get("tool_name"),
        "reasoning": state.get("reasoning", []),
    }