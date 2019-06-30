from collections import deque


class DefaultQueue:
	"""LIFO queue class that takes a producer function as input."""
	def __init__(self, default_func):
		self._dq = deque()
		self.default_func = default_func

	def add_right(self, item):
		self._dq.append(item)

	def pop_left(self):
		if self._dq:
			return self._dq.popleft()

		return self.default_func()
