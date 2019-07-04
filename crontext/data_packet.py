"""File that contains DataPacket and extending classes. These classes exist to be
stable, immutable data structures that can be sent between threads.
"""


class DataPacket:
	"""Parent interface that stores some kind of data that can be transported
	between threads.
	"""
	pass


class TextPacket(DataPacket):
	def __init__(self, text: str, text_id: int) -> None:
		self.text = text
		self.id = text_id


class ReschedulePacket(DataPacket):
	def __init__(self, time):
		self.time = time
