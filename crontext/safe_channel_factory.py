
from crontext.safe_queue import SafeQueue
from crontext.safe_channel import SafeChannel


class SafeChannelFactory:
    def __init__(self):
        self.queue1 = SafeQueue()
        self.queue2 = SafeQueue()

    def make_channel1(self):
        return SafeChannel(self.queue1, self.queue2)

    def make_channel2(self):
        return SafeChannel(self.queue2, self.queue1)
