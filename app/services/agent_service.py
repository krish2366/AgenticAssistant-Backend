from app.agents.graph import build_graph 
from app.agents.state import AgentState

class AgentService:
    def __init__(self) -> None:
        self.agent = build_graph()
        
    def ask(self, project_id: str, question: str) -> dict:
        initial_state : AgentState = {
            "project_id" : project_id,
            "question" : question,
            "retrieved_chunks" : [],
            "reasoning" : [],
            "answer": "",            
        }
        
        
        result = self.agent.invoke(initial_state)

        return {
            "answer" : result.get("answer",""),
            "tool_used" : result.get("tool_name"),
            "reasoning" : result.get("reasoning",[])
        }
        
agent_service = AgentService()