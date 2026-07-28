"""
AsterSurge Provider Factory

Version: 0.3.0
"""

from .config import Config
from .validators import Validator
from .providers import (
    GroqProvider,
    OpenAIProvider,
    GeminiProvider,
    OllamaProvider,
)


class ProviderFactory:
    """
    Factory responsible for creating LLM providers.
    """

    _providers = {
        "groq": GroqProvider,
        "openai": OpenAIProvider,
        "gemini": GeminiProvider,
        "ollama": OllamaProvider,
    }

    @classmethod
    def create(
        cls,
        provider=None,
        model=None,
        **kwargs,
    ):
        """
        Create a provider instance.
        """

        provider = (
            provider
            or Config.PROVIDER
        ).lower()

        Validator.provider(
            provider,
            cls._providers.keys(),
        )

        provider_class = cls._providers[
            provider
        ]

        if model is None:
            model = Config.MODEL

        return provider_class(
            model=model,
            **kwargs,
        )

    @classmethod
    def register(
        cls,
        name,
        provider_class,
    ):
        """
        Register a custom provider.
        """

        cls._providers[
            name.lower()
        ] = provider_class

    @classmethod
    def unregister(
        cls,
        name,
    ):
        """
        Remove a provider.
        """

        cls._providers.pop(
            name.lower(),
            None,
        )

    @classmethod
    def available(cls):
        """
        Return available providers.
        """

        return sorted(
            cls._providers.keys()
        )

    @classmethod
    def exists(
        cls,
        name,
    ):
        """
        Check whether a provider exists.
        """

        return (
            name.lower()
            in cls._providers
        )
