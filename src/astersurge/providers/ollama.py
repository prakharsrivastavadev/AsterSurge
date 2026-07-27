"""
Ollama Provider

AsterSurge v0.2
"""

import requests

from .base import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Ollama LLM Provider
    """

    def __init__(
        self,
        model="llama3.2",
        host="http://localhost:11434",
    ):
        super().__init__(model)
        self.host = host

    def generate(
        self,
        prompt: str,
        system_prompt="You are AsterSurge AI.",
    ) -> str:

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": f"{system_prompt}\n\n{prompt}",
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "")
