
from crontext.safe_queue import SafeQueue


class SafeChannel:
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
