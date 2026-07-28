"""
AsterSurge Router

Version: 0.2.0
"""


class Router:
    """
    Routes tasks to the appropriate provider or tool.
    """

    def __init__(self):
        self._routes = {}

    def register(self, name: str, handler):
        """
        Register a handler.
        """
        self._routes[name] = handler

    def unregister(self, name: str):
        """
        Remove a handler.
        """
        self._routes.pop(name, None)

    def get(self, name: str):
        """
        Get a handler.
        """
        return self._routes.get(name)

    def dispatch(self, name: str, *args, **kwargs):
        """
        Execute a registered handler.
        """
        handler = self.get(name)

        if handler is None:
            raise ValueError(
                f"No route registered for '{name}'."
            )

        return handler(*args, **kwargs)

    def routes(self):
        """
        Return registered routes.
        """
        return sorted(self._routes.keys())

    def clear(self):
        """
        Remove all routes.
        """
        self._routes.clear()
