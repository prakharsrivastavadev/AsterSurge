"""
AsterSurge Serializer

Version: 0.2.0
"""

import json
from pathlib import Path


class Serializer:
    """
    JSON serialization utilities.
    """

    @staticmethod
    def dumps(data, indent=4):
        """
        Convert Python object to JSON string.
        """
        return json.dumps(
            data,
            indent=indent,
            ensure_ascii=False,
        )

    @staticmethod
    def loads(text):
        """
        Convert JSON string to Python object.
        """
        return json.loads(text)

    @staticmethod
    def save(path, data):
        """
        Save JSON to a file.
        """
        path = Path(path)

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    @staticmethod
    def load(path):
        """
        Load JSON from a file.
        """
        path = Path(path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    @staticmethod
    def pretty(data):
        """
        Return formatted JSON.
        """
        return Serializer.dumps(data, indent=4)
