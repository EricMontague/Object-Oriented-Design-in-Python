from abc import ABC, abstractmethod
from enum import Enum


class ChatType(Enum):

    GROUP_CHAT = 0
    PRIVATE_CHAT = 1


class Chat(ABC):
    def __init__(self, chat_id, chat_name, chat_type):
        self._chat_id = chat_id
        self._chat_name = chat_name
        self._chat_type = chat_type
        self._members_by_id = {}
        self._messages = []

    @abstractmethod
    def send_message(self, message):
        pass

    def add_member(self, user):
        self._members_by_id[user.id] = user

    def remove_member(self, user_id):
        if user_id in self._members_by_id:
            self._members_by_id.pop(user_id)

    @property
    def chat_id(self):
        return self._chat_id

    @property
    def name(self):
        return self._chat_name

    @name.setter
    def name(self, name):
        self._chat_name = name

    @property
    def chat_type(self):
        return self._chat_type


class GroupChat(Chat):
    def __init__(self, chat_id, chat_name, chat_type):
        super().__init__(chat_id, chat_name, chat_type)

    def send_message(self, message):
        for member in self._members_by_id:
            self._messages.append(message)
            self._members_by_id[member].receive_message(
                message.from_user.user_id, message.text
            )


class PrivateChat(Chat):
    def __init__(self, chat_id, chat_name, chat_type, first_user, second_user):
        super().__init__(chat_id, chat_name, chat_type)
        self._members_by_id[first_user.user_id] = first_user
        self._members_by_id[second_user.user_id] = second_user

    def send_message(self, message):
        self._messages.append(message)
        self._members_by_id[message.to_user.user_id].receive_message(
            message.from_user.user_id, message.text
        )
