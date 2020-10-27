from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def receive_notification(self, notification):
        pass

