from friend_request import FriendRequestStatus
from invite import ChatInvite
from chats import PrivateChat, GroupChat, ChatType
from message import Message, GroupMessage


class User:
    def __init__(self, user_id, name, password_hash):
        self._user_id = user_id
        self._name = name
        self._password_hash = password_hash
        self._friends_by_id = {}
        self._sent_friend_requests_by_friend_id = {}
        self._received_friend_requests_by_friend_id = {}
        self._group_chats_by_id = {}
        self._private_chats_by_friend_id = {}

    def add_friend(self, user):
        self._friends_by_id[user.user_id] = user

    def remove_friend(self, user_id):
        user = self._friends_by_id.get(user_id)
        if user:
            self._friends_by_id.pop(user_id)

    def make_friend_request(self, request):
        self._sent_friend_requests_by_friend_id[request.to_user.user_id] = request

    def receive_friend_request(self, request):
        request.status = FriendRequestStatus.READ
        self._received_friend_requests_by_friend_id[request.from_user.user_id] = request

    def approve_friend_request(self, user_id):
        request = self._received_friend_requests_by_friend_id.get(user_id)
        if request:
            self._friends_by_id[request.user_id] = request.from_user
            request.status = FriendRequestStatus.ACCEPTED
        ValueError("Request not found")

    def reject_friend_request(self, user_id):
        request = self._received_friend_requests_by_friend_id.get(user_id)
        if request:
            request.status = FriendRequestStatus.REJECTED

    def create_group_chat(self):
        group_chat = GroupChat(
            "random_chat_id", "The best group chat", ChatType.GROUP_CHAT
        )
        group_chat.add_member(self)
        self._group_chats_by_id[group_chat.chat_id] = group_chat

    def invite_to_group_chat(self, user_id, chat_id):
        friend = self._friends_by_id.get(user_id)
        if not friend:
            raise ValueError("Friend not found")
        group_chat = self._group_chats_by_id.get(chat_id)
        if not group_chat:
            raise ValueError("Group chat not found")
        invite = ChatInvite(self, friend, group_chat)
        friend.receive_chat_invite(invite)

    def invite_to_private_chat(self, user_id):
        friend = self._friends_by_id.get(user_id)
        if not friend:
            raise ValueError("Friend not found")
        private_chat = PrivateChat(
            "random_chat_id", "The best chat", ChatType.PRIVATE_CHAT, self, friend
        )
        invite = ChatInvite(self, friend, private_chat)
        friend.receive_chat_invite(invite)

    def receive_chat_invite(self, invite):
        if invite.chat.chat_type == ChatType.GROUP_CHAT:
            invite.group_chat.add_member(self)
            self._group_chats_by_id[invite.group_chat.chat_id] = invite.group_chat
        elif invite.chat.chat_type == ChatType.PRIVATE_CHAT:
            self._private_chats_by_friend_id[invite.private_chat.chat_id] = invite.private_chat

    def leave_chat(self, chat_id):
        chat = None
        if chat_id in self._group_chats_by_id:
            chat = self._group_chats_by_id.pop(chat_id)
        elif chat_id in self._private_chats_by_friend_id:
            chat = self._private_chats_by_friend_id.pop(chat_id)
        if not chat:
            raise ValueError("Chat not found")
        chat.remove_member(self._user_id)

    def message_group(self, chat_id, text):
        group_chat = self._group_chats_by_id.get(chat_id)
        if not group_chat:
            raise ValueError("Group chat not found")
        message = GroupMessage("random_message_id", self, text)
        group_chat.send_message(message)

    def message_user(self, user_id, text):
        private_chat = self._private_chats_by_friend_id.get(user_id)
        friend = self._friends_by_id.get(user_id)
        if not private_chat:
            raise ValueError("Private chat not found")
        if not user:
            raise ValueError("Friend not found")
        message = Message("random_message_id", self, friend, text)
        private_chat.send_message(message)

