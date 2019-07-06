"""Module that contains the safe channel class and a factory to create
instances of it.
"""
from crontext.broker.safe_queue import SafeQueue


class Broker:
    def __init__(self, in_queue: SafeQueue, out_queue: SafeQueue) -> None:
        self._in_queue = in_queue
        self._out_queue = out_queue

    def get(self):
        return self._in_queue.get()

    def put(self, item):
        self._out_queue.put(item)

    def remove_and(self, func):
        self._in_queue.remove_and(func)

    def remove_all_and(self, func):
        self._in_queue.remove_all_and(func)


class BrokerFactory:
    def __init__(self):
        self._queue1 = SafeQueue()
        self._queue2 = SafeQueue()

    def make_channel1(self):
        return Broker(self._queue1, self._queue2)

    def make_channel2(self):
        return Broker(self._queue2, self._queue1)
