"""
Google Gemini Provider

AsterSurge v0.2
"""

import os

import google.generativeai as genai

from .base import BaseProvider


class GeminiProvider(BaseProvider):
    """
    Google Gemini Provider
    """

    def __init__(
        self,
        model="gemini-2.5-flash",
        api_key=None,
    ):
        super().__init__(model)

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable not found."
            )

        genai.configure(api_key=self.api_key)

        self.client = genai.GenerativeModel(self.model)

    def generate(
        self,
        prompt: str,
        system_prompt="You are AsterSurge AI.",
    ) -> str:

        full_prompt = f"{system_prompt}\n\n{prompt}"

        response = self.client.generate_content(full_prompt)

        return response.text
