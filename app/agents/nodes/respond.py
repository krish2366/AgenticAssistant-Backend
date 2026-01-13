from app.agents.state import AgentState

def respond_node(state: AgentState) -> dict:
    explanation = f"""
        Answer: {state["answer"]}

        Tool Used: {state.get('tool_name')}
        Reasoning Trail:
        {state.get('reasoning')}
        """

    return {
        "answer": explanation,
        "tool_name": state.get("tool_name"),
        "reasoning": state.get("reasoning", []),
    }