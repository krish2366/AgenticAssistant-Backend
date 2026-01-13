from app.llms.gemini import GeminiLLM
from app.agents.state import AgentState


llm = GeminiLLM()

def analyze_node(state: AgentState) -> dict:
    answer = llm.generate(
        question=f"""
        User Question:
        {state["question"]}

        Tool Used:
        {state.get("tool_name")}

        Tool Output:
        {state.get("tool_result")}

        Provide a clear, helpful answer.
        Explain briefly why this tool was used.
        Mention any risks or side effects if applicable.
        """,
        context_chunks= state["retrieved_chunks"]
    )
    
    return {
        "answer": answer,
        "reasoning": state["reasoning"] + [
            "Final analysis performed using tool output"
        ]
    }