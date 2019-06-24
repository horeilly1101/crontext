"""File that contains the SafeQueue class."""

import threading
from collections import deque


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

	def empty(self):
		with self._lock:
			return len(self._deque) == 0

	def get_and(self, func):
		func(self.get())

	def get_each_and(self, func):
		with self._lock:
			for _ in self._deque:
				func(self._deque.pop())
