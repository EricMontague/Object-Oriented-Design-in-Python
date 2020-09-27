from datetime import datetime


class ChatInvite:

    def __init__(self, from_user, to_user, chat):
        self._from_user = from_user
        self._to_user = to_user
        self._chat = chat
        self._timestamp = datetime.now()

    @property
    def from_user(self):
        return self._from_user
    
    @property
    def to_user(self):
        return self._to_user

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def chat(self):
        return self._chat
