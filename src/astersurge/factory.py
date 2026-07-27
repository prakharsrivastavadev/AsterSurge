"""
AsterSurge Provider Factory

Creates provider instances from configuration.
"""

from .providers import (
    GroqProvider,
    OpenAIProvider,
    GeminiProvider,
    OllamaProvider,
)


class ProviderFactory:
    """
    Factory for creating LLM providers.
    """

    PROVIDERS = {
        "groq": GroqProvider,
        "openai": OpenAIProvider,
        "gemini": GeminiProvider,
        "ollama": OllamaProvider,
    }

    @classmethod
    def create(cls, provider: str, **kwargs):
        """
        Create a provider instance.

        Example:
            ProviderFactory.create("groq")
        """

        provider = provider.lower()

        if provider not in cls.PROVIDERS:
            available = ", ".join(cls.PROVIDERS.keys())
            raise ValueError(
                f"Unknown provider '{provider}'. "
                f"Available providers: {available}"
            )

        return cls.PROVIDERS[provider](**kwargs)

    @classmethod
    def available(cls):
        """
        Return available providers.
        """

        return sorted(cls.PROVIDERS.keys())
