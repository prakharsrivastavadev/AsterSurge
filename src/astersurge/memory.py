"""
AsterSurge Memory

Simple in-memory conversation storage.

Version: 0.1
"""


class Memory:
    """Stores conversation history."""

    def __init__(self):
        self._messages = []

    def add(self, role: str, content: str):
        """
        Add a message to memory.

        Parameters
        ----------
        role : str
            "user", "assistant", or "system"

        content : str
            Message content.
        """

        self._messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def history(self):
        """
        Return conversation history.
        """

        return self._messages.copy()

    def last(self):
        """
        Return the latest message.
        """

        if not self._messages:
            return None

        return self._messages[-1]

    def clear(self):
        """
        Clear all stored messages.
        """

        self._messages.clear()

    def size(self):
        """
        Return number of stored messages.
        """

        return len(self._messages)
