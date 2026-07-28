"""
AsterSurge Models

Version: 0.3.0
"""

from .factory import ProviderFactory


class Model:
    """
    Wrapper around a language model provider.
    """

    def __init__(
        self,
        provider="groq",
        model=None,
    ):
        self.provider_name = provider

        self.provider = ProviderFactory.create(
            provider,
            model=model,
        )

    def generate(
        self,
        prompt: str,
        system_prompt="You are AsterSurge AI.",
        **kwargs,
    ):
        """
        Generate a response.
        """

        return self.provider.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            **kwargs,
        )


class ModelManager:
    """
    Manage multiple models.
    """

    def __init__(self):
        self._models = {}

    def register(
        self,
        name,
        provider="groq",
        model=None,
    ):
        self._models[name] = Model(
            provider=provider,
            model=model,
        )

    def get(self, name):
        return self._models.get(name)

    def generate(
        self,
        name,
        prompt,
        **kwargs,
    ):
        model = self.get(name)

        if model is None:
            raise ValueError(
                f"Model '{name}' is not registered."
            )

        return model.generate(
            prompt,
            **kwargs,
        )

    def unregister(self, name):
        self._models.pop(name, None)

    def list(self):
        return sorted(self._models.keys())

    def clear(self):
        self._models.clear()

    def count(self):
        return len(self._models)
