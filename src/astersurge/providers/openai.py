"""
OpenAI Provider

AsterSurge v0.2
"""

import os

from openai import OpenAI

from .base import BaseProvider


class OpenAIProvider(BaseProvider):
    """
    OpenAI LLM Provider
    """

    def __init__(
        self,
        model="gpt-4.1-mini",
        api_key=None,
    ):
        super().__init__(model)

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable not found."
            )

        self.client = OpenAI(
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
