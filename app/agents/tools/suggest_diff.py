from app.llms.gemini import GeminiLLM
from app.agents.state import AgentState

llm = GeminiLLM()

def suggest_diff_node(state: AgentState) -> dict:
    content = "\n\n".join(state["retrieved_chunks"])

    diff = llm.generate(
        question=f"""
        You are a senior software engineer.

        Task:
        Suggest a SAFE code diff based on the user's request.

        User Request:
        {state["question"]}

        Rules:
        - Do NOT rewrite entire files
        - Show only relevant changes
        - Use diff-style formatting where possible
        - Mention which files are affected
        - Warn about possible side effects
        """,
        context_chunks=[content],
    )

    return {
        "tool_name": "suggest_diff",
        "tool_input": state["question"],
        "tool_result": diff,
        "reasoning": state["reasoning"] + [
            "suggest_diff selected because the user asked for a code change/refactor",
            "LLM analyzed retrieved code and generated a non-destructive diff suggestion",
        ],
    }
