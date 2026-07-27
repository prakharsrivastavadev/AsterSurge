"""
AsterSurge Plugin System

Version: 0.2.0
"""


class Plugin:
    """
    Base plugin class.
    """

    name = "plugin"
    version = "0.1.0"

    def setup(self):
        """
        Initialize plugin.
        """
        pass


class PluginManager:
    """
    Registers and manages plugins.
    """

    def __init__(self):
        self._plugins = {}

    def register(self, plugin):
        self._plugins[plugin.name] = plugin
        plugin.setup()

    def unregister(self, name):
        if name in self._plugins:
            del self._plugins[name]

    def get(self, name):
        return self._plugins.get(name)

    def all(self):
        return list(self._plugins.values())

    def names(self):
        return sorted(self._plugins.keys())

    def count(self):
        return len(self._plugins)
