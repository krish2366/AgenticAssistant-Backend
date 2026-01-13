from app.llms.base import BaseLLM


class OllamaLLM(BaseLLM):
    def generate(self, question: str, context_chunks: list[str]) -> str:
        raise NotImplementedError("Ollama support added later")
