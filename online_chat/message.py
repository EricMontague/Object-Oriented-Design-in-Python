from datetime import datetime

class Message:
    def __init__(self, message_id, from_user, to_user, text):
        self._message_id = message_id
        self._from_user = from_user
        self._to_user = to_user
        self._text = text
        self._timestamp = datetime.now()
        self._read = False

    @property
    def from_user(self):
        return self._from_user

    @property
    def to_user(self):
        return self._to_user

    @property
    def text(self):
        return self._text

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def message_id(self):
        return self._message_id

    def was_read(self):
        return self._read
    
    def mark_as_read(self):
        self._read = True



class GroupMessage:
    def __init__(self, message_id, from_user, text):
        self._message_id = message_id
        self._from_user = from_user
        self._text = text
        self._read_by = []

    @property
    def from_user(self):
        return self._from_user

    @property
    def text(self):
        return self._text

    @property
    def message_id(self):
        return self._message_id
    
    def mark_as_read_by(self, user):
        self._read_by.append(user)