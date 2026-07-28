"""
AsterSurge Prompts

Version: 0.2.0
"""


class Prompts:
    """
    Built-in prompt templates.
    """

    SYSTEM = (
        "You are AsterSurge, an intelligent AI assistant. "
        "Be accurate, concise, and helpful."
    )

    PLANNER = (
        "Break the user's request into clear executable steps."
    )

    CODER = (
        "Write clean, maintainable, and well-documented code."
    )

    REVIEWER = (
        "Review the provided content and suggest improvements."
    )

    SUMMARIZER = (
        "Summarize the provided text while preserving key information."
    )

    TRANSLATOR = (
        "Translate the text while preserving meaning and tone."
    )

    EXPLAINER = (
        "Explain the concept clearly with examples."
    )

    @classmethod
    def get(cls, name: str):
        """
        Return a prompt by name.
        """
        return getattr(cls, name.upper(), cls.SYSTEM)

    @classmethod
    def list(cls):
        """
        Return available prompt names.
        """
        return [
            "system",
            "planner",
            "coder",
            "reviewer",
            "summarizer",
            "translator",
            "explainer",
        ]
