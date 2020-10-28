from abc import ABC, abstractmethod


class ISubject(ABC):
    def __init__(self):
        self._observers = {}

    @abstractmethod
    def notify_observers(self, data):
        pass

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer_id):
        pass

