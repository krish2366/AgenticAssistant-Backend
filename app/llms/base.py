from abc import ABC, abstractmethod 
from typing import List


class BaseLLM(ABC):
    @abstractmethod
    def generate(self, question: str, context_chunks: List[str]) -> str:
        pass
        