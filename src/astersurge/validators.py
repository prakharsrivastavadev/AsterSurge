"""
AsterSurge Validators

Version: 0.2.0
"""

from pathlib import Path


class Validator:
    """
    Common validation utilities.
    """

    @staticmethod
    def not_empty(value, name="value"):
        if value is None:
            raise ValueError(f"{name} cannot be None.")

        if isinstance(value, str) and not value.strip():
            raise ValueError(f"{name} cannot be empty.")

        return value

    @staticmethod
    def provider(name, available):
        Validator.not_empty(name, "provider")

        if name not in available:
            raise ValueError(
                f"Unknown provider '{name}'. "
                f"Available: {', '.join(sorted(available))}"
            )

        return name

    @staticmethod
    def file_exists(path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        return path

    @staticmethod
    def positive_int(value, name="value"):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")

        if value <= 0:
            raise ValueError(f"{name} must be greater than zero.")

        return value

    @staticmethod
    def percentage(value):
        if not 0 <= value <= 1:
            raise ValueError(
                "Value must be between 0 and 1."
            )

        return value
