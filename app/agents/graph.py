from langgraph.graph import StateGraph, END 
from app.agents.state import AgentState
from app.agents.nodes.analyze import analyze_node
from app.agents.nodes.respond import respond_node
from app.agents.nodes.retrieve import retrieve_node
from app.agents.tools.router import router_node
from app.agents.tools.search_file import search_file_node
from app.agents.tools.suggest_diff import suggest_diff_node
 

def build_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("router", router_node)

    graph.add_node("search_file", search_file_node)
    graph.add_node("suggest_diff", suggest_diff_node)

    graph.add_node("analyze", analyze_node)
    graph.add_node("respond", respond_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "router")
    
    graph.add_conditional_edges(
        "router",
        lambda s: s.get("tool_name"),
        {
            "search_file": "search_file",
            "suggest_diff": "suggest_diff",
        }
    )
    graph.add_edge("search_file", "analyze")
    graph.add_edge("suggest_diff", "analyze")

    graph.add_edge("analyze", "respond")
    graph.add_edge("respond", END)

    return graph.compile()