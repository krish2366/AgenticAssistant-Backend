from typing import List
from google import genai 
from app.config import GEMINI_API_KEY
from app.llms.base import BaseLLM

 
class GeminiLLM(BaseLLM):
    def __init__(self) -> None:
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model_name = "models/gemini-2.5-flash"
        
    def generate(self, question: str, context_chunks: List[str]) -> str:
        if not question or not question.strip():
            raise ValueError("No question asked!!!")
        if not context_chunks:
            raise ValueError("No context provided!!!")
        
        context = "\n\n".join(context_chunks)
        
        prompt = f"""
            You are a senior software engineer.
            Answer the question using ONLY the provided code context.

            Code Context:
            {context}

            Question:
            {question}

            Rules:
            - Be precise
            - Mention file paths when relevant
            - Do NOT hallucinate, if context not present simply say so.
        """
        
        response = self.client.models.generate_content(
            model= self.model_name,
            contents= prompt
        )
        
        return response.text.strip()