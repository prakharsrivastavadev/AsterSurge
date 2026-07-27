"""
AsterSurge Events

Version: 0.2.0
"""

from collections import defaultdict
from typing import Callable, Dict, List


class EventBus:
    """
    Simple publish/subscribe event bus.
    """

    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable):
        """
        Subscribe to an event.
        """
        if callback not in self._listeners[event]:
            self._listeners[event].append(callback)

    def unsubscribe(self, event: str, callback: Callable):
        """
        Remove a listener.
        """
        if callback in self._listeners[event]:
            self._listeners[event].remove(callback)

    def emit(self, event: str, *args, **kwargs):
        """
        Emit an event to all listeners.
        """
        for callback in self._listeners[event]:
            callback(*args, **kwargs)

    def listeners(self, event: str):
        """
        Return listeners for an event.
        """
        return list(self._listeners.get(event, []))

    def clear(self):
        """
        Remove all registered listeners.
        """
        self._listeners.clear()

    def events(self):
        """
        Return registered event names.
        """
        return sorted(self._listeners.keys())
