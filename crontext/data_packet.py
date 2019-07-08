"""File that contains DataPacket and extending classes. These classes exist to be
stable, immutable data structures that can be sent between threads.

NOTE: The classes in this module comprise the API for how the server and the worker
interact with each other.
"""
import datetime


class DataPacket:
    """Parent interface that stores some kind of data that can be transported
    between threads.
    """
    pass


class TextPacket(DataPacket):
    def __init__(self, text: str, text_id: int) -> None:
        self.text = text
        self.id = text_id

    def __str__(self):
        return "TextPacket(text={}, id={})".format(self.text, self.id)


class ReceiptPacket(DataPacket):
    def __init__(self, text: str, sent_at: datetime, text_id: int) -> None:
        self.text = text
        self.sent_at = sent_at
        self.id = text_id


class ReschedulePacket(DataPacket):
    def __init__(self, time):
        self.time = time
