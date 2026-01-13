from app.rag.retrieval import retrieve

PROJECT_ID = "3798c527-1a73-458b-a94a-26f079afe3f9"

results = retrieve(
    project_id=PROJECT_ID,
    question="Where is editing of file is handled?"
)

for r in results:
    print("FILE:", r["file_path"])
    print("CONTENT:", r["content"][:200])
    print("-" * 50)