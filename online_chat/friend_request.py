from datetime import datetime
from enum import Enum


class FriendRequestStatus(Enum):

    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3


class FriendRequest:
    def __init__(self, from_user, to_user):
        self._from_user = from_user
        self._to_user = to_user
        self._timestamp = datetime.now()
        self._status = FriendRequestStatus.UNREAD

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
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
