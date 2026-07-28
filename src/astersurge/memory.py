"""
AsterSurge Memory

Version: 0.3.0
"""

from pathlib import Path
import json


class Memory:
    """
    Persistent conversation memory.
    """

    def __init__(
        self,
        path="memory.json",
    ):
        self.path = Path(path)
        self.messages = []

        self.load()

    def add(
        self,
        role,
        content,
    ):
        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

        self.save()

    def history(self):
        return self.messages

    def last(self):
        if self.messages:
            return self.messages[-1]

        return None

    def clear(self):
        self.messages.clear()
        self.save()

    def size(self):
        return len(self.messages)

    def save(self):
        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self.messages,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(self):
        if not self.path.exists():
            return

        try:
            with self.path.open(
                "r",
                encoding="utf-8",
            ) as file:
                self.messages = json.load(file)

        except Exception:
            self.messages = []
