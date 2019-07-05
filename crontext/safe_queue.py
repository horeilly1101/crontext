"""File that contains the SafeQueue class."""

import threading
from collections import deque
from copy import copy


class SafeQueue:
    """This class exists to be a thread-safe message channel between multiple
    threads. It acts like a FIFO queue.
    """
    def __init__(self):
        """Initialize a SafeQueue."""
        self._lock = threading.RLock()
        self._deque = deque()

    def get(self):
        """Pop the next item of the queue and return it.
        :return: the next item from the queue
        """
        with self._lock:
            return self._deque.popleft()

    def put(self, item) -> None:
        """Put the input item into the queue.
        :param item: item to be added to queue
        """
        with self._lock:
            self._deque.append(item)

    def is_empty(self) -> bool:
        """
        :return: whether or not there are any items stored in the queue. NOTE: This method returning True
        does no guarantee that a subsequent "get" won't throw an exception.
        """
        with self._lock:
            return len(self._deque) == 0

    def remove_and(self, func) -> None:
        """Remove an item from the queue and apply the input function to it.
        :param func: function to be applied to the next item on the queue
        """
        func(self.get())

    def remove_all_and(self, func) -> None:
        """Remove all items from the queue and apply the input function to each item.
        :param func: function to be applied to the next item on the queue
        """
        # NOTE: the use of an RLock prevents deadlock and ensures thread safety
        with self._lock:
            for _ in copy(self._deque):
                self.remove_and(func)
