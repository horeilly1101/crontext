"""define an immutable data structure that can be sent in the queue."""


class Message:
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return self.text
