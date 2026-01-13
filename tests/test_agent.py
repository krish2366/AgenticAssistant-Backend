# from app.agents.graph import build_graph

# agent = build_graph()

# result = agent.invoke({
#     "project_id": "3798c527-1a73-458b-a94a-26f079afe3f9",
#     "question": "Where is file editing is handled?",
#     "retrieved_chunks": [],
#     "answer": ""
# })

# print(result["answer"])

from app.agents.graph import build_graph

agent = build_graph()

result = agent.invoke({
    "project_id": "3798c527-1a73-458b-a94a-26f079afe3f9",
    "question": "Suggest a refactor for authentication",
    "retrieved_chunks": [],
    "reasoning": [],
})
try:
    print(result)
except Exception as e:
    print(str(e))