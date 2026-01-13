from typing import TypedDict, List, Optional

class AgentState(TypedDict, total = False):
    project_id: str
    question: str
    retrieved_chunks: List[str]
    answer: str
    tool_name: Optional[str]
    tool_input: Optional[str]
    tool_result: Optional[str]
    reasoning: List[str]