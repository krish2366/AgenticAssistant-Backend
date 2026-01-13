from app.llms.gemini import GeminiLLM 

llm = GeminiLLM()
print(llm.generate(
    "What does this code do?",
    ["def login(): pass"]
))
