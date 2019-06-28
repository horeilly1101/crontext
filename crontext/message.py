"""define a data structure that can be sent in the queue."""


class Message:
	def __init__(self, storage):
		self.storage = storage

	def __str__(self):
		return "{0}(storage={1})".format(self.__name__, self.storage)


class TextMessage(Message):
	def __init__(self, text):
		super().__init__(text)


class RescheduleMessage(Message):
	def __init__(self, time):
		super().__init__(time)
