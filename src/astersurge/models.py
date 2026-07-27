"""
AsterSurge Models

Model abstraction layer.

Version: 0.1
"""


class BaseModel:
    """Base interface for all language models."""

    def __init__(self, name="base-model"):
        self.name = name

    def generate(self, prompt: str):
        """
        Generate a response.

        Must be implemented by subclasses.
        """
        raise NotImplementedError(
            "Subclasses must implement generate()."
        )


class EchoModel(BaseModel):
    """
    Simple demonstration model.

    Returns the prompt without modification.
    """

    def __init__(self):
        super().__init__("echo")

    def generate(self, prompt: str):
        return prompt


class ModelManager:
    """
    Registers and retrieves models.
    """

    def __init__(self):

        self._models = {}

        self.register(EchoModel())

    def register(self, model: BaseModel):

        self._models[model.name] = model

    def get(self, name: str):

        return self._models.get(name)

    def available(self):

        return sorted(self._models.keys())

    def generate(self, model_name: str, prompt: str):

        model = self.get(model_name)

        if model is None:
            raise ValueError(
                f"Unknown model: {model_name}"
            )

        return model.generate(prompt)
