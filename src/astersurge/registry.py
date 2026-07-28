"""
AsterSurge Registry

Version: 0.2.0
"""


class Registry:
    """
    Central registry for AsterSurge components.
    """

    def __init__(self):
        self._items = {}

    def register(self, category: str, name: str, item):
        """
        Register an item under a category.
        """
        self._items.setdefault(category, {})
        self._items[category][name] = item

    def unregister(self, category: str, name: str):
        """
        Remove an item.
        """
        if category in self._items:
            self._items[category].pop(name, None)

    def get(self, category: str, name: str):
        """
        Get a registered item.
        """
        return self._items.get(category, {}).get(name)

    def list(self, category: str):
        """
        List names in a category.
        """
        return sorted(self._items.get(category, {}).keys())

    def categories(self):
        """
        Return all categories.
        """
        return sorted(self._items.keys())

    def clear(self):
        """
        Remove everything.
        """
        self._items.clear()

    def count(self):
        """
        Return total registered items.
        """
        return sum(len(items) for items in self._items.values())
