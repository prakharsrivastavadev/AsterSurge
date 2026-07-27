"""
AsterSurge Storage

Version: 0.2.0
"""

from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Base storage interface.
    """

    @abstractmethod
    def save(self, key: str, value):
        pass

    @abstractmethod
    def load(self, key: str):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass

    @abstractmethod
    def exists(self, key: str):
        pass


class MemoryStorage(Storage):
    """
    In-memory storage implementation.
    """

    def __init__(self):
        self._data = {}

    def save(self, key: str, value):
        self._data[key] = value

    def load(self, key: str):
        return self._data.get(key)

    def delete(self, key: str):
        self._data.pop(key, None)

    def exists(self, key: str):
        return key in self._data

    def keys(self):
        return list(self._data.keys())

    def clear(self):
        self._data.clear()

    def size(self):
        return len(self._data)
