"""
AsterSurge Cache

Version: 0.2.0
"""


class Cache:
    """
    Simple in-memory cache.
    """

    def __init__(self):
        self._cache = {}

    def set(self, key, value):
        """
        Store a value.
        """
        self._cache[key] = value

    def get(self, key, default=None):
        """
        Retrieve a value.
        """
        return self._cache.get(key, default)

    def exists(self, key):
        """
        Check if key exists.
        """
        return key in self._cache

    def delete(self, key):
        """
        Delete a cached value.
        """
        if key in self._cache:
            del self._cache[key]

    def clear(self):
        """
        Clear the cache.
        """
        self._cache.clear()

    def keys(self):
        """
        Return all cache keys.
        """
        return list(self._cache.keys())

    def values(self):
        """
        Return all cached values.
        """
        return list(self._cache.values())

    def items(self):
        """
        Return key-value pairs.
        """
        return self._cache.items()

    def size(self):
        """
        Return cache size.
        """
        return len(self._cache)
