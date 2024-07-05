from abc import ABC, abstractmethod


class SinkClient(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def send_message(self, message, key):
        pass
