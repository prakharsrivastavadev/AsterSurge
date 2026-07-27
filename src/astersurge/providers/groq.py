"""
Groq Provider

AsterSurge v0.2
"""

import os

from groq import Groq

from .base import BaseProvider


class GroqProvider(BaseProvider):
    """
    Groq LLM Provider
    """

    def __init__(
        self,
        model="llama-3.3-70b-versatile",
        api_key=None,
    ):
        super().__init__(model)

        self.api_key = api_key or os.getenv("GROQ_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GROQ_API_KEY environment variable not found."
            )

        self.client = Groq(
            api_key=self.api_key
        )

    def generate(
        self,
        prompt: str,
        system_prompt="You are AsterSurge AI.",
        temperature=0.2,
        max_tokens=1024,
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content
