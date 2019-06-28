"""File that contains the SafeQueue class."""

import threading
from collections import deque
from copy import copy


class SafeQueue:
	"""This class exists to be a thread-safe channel between multiple threads."""
	def __init__(self):
		self._lock = threading.RLock()
		self._deque = deque()

	def get(self):
		with self._lock:
			return self._deque.popleft()

	def put(self, item):
		with self._lock:
			return self._deque.append(item)

	def is_empty(self):
		with self._lock:
			return len(self._deque) == 0

	def get_and(self, func):
		return func(self.get())

	def empty_and(self, func):
		with self._lock:
			for _ in copy(self._deque):
				self.get_and(func)
