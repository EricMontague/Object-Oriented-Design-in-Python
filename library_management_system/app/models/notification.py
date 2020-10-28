from datetime import datetime


class Notification:
    def __init__(self, message, receiver):
        self._message = message
        self._receiver = receiver
        self._created_at = datetime.now()

    @property
    def message(self):
        return self._message

    @property
    def receiver(self):
        return self._receiver

    @property
    def send_on_date(self):
        return self._created_at
