"""
Base LLM Provider

Every model provider should inherit from this class.
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract interface for language model providers.
    """

    def __init__(self, model: str):
        self.model = model

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the model.
        """
        pass
