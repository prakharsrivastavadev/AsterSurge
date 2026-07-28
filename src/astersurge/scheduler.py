"""
AsterSurge Scheduler

Version: 0.2.0
"""

import time
from threading import Thread


class Scheduler:
    """
    Simple task scheduler.
    """

    def __init__(self):
        self._tasks = []

    def schedule(self, delay, func, *args, **kwargs):
        """
        Schedule a task after a delay.
        """

        def runner():
            time.sleep(delay)
            func(*args, **kwargs)

        thread = Thread(target=runner, daemon=True)
        thread.start()

        self._tasks.append(thread)

        return thread

    def wait(self):
        """
        Wait for all scheduled tasks.
        """

        for task in self._tasks:
            task.join()

    def clear(self):
        """
        Clear completed tasks.
        """

        self._tasks = [
            task
            for task in self._tasks
            if task.is_alive()
        ]

    def count(self):
        """
        Return number of tracked tasks.
        """

        return len(self._tasks)
