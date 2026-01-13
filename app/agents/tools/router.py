from app.llms.gemini import GeminiLLM
from app.agents.state import AgentState

llm = GeminiLLM()

def router_node(state: AgentState) -> dict:
    prompt = f"""
    You have two tools: search_file, suggest_diff.
    User question: {state['question']}
    Decide which tool best helps achieve the goal, and respond with exactly one tool name.
    """

    decision = llm.generate(question=prompt, context_chunks=state["retrieved_chunks"])

    tool = decision.strip().lower()

    return {"tool_name": tool}
