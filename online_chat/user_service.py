from friend_request import FriendRequest

class UserService:
    def __init__(self):
        self._users_by_id = {}

    def add_user(self, user):
        self._users_by_id[user.user_id] = user

    def update_user(self, user_id, payload):
        user = self._users_by_id.get(user_id)
        if not user:
            raise ValueError("User not found")
        user.name = payload.name

    def remove_user(self, user_id):
        if user_id not in self._users_by_id:
            raise ValueError("User not found")
        self._users_by_id.pop(user_id)

    def make_friend_request(self, from_user_id, to_user_id):
        from_user = self._users_by_id.get(from_user_id)
        to_user = self._users_by_id.get(to_user_id)
        if not from_user:
            raise ValueError("User creating the request was not found")
        if not to_user:
            raise ValueError("User for who the request is for was not found")
        request = FriendRequest(from_user, to_user)
        from_user.make_friend_request(request)
        to_user_id.receive_from_request(request)

    def approve_friend_request(self, from_user_id, to_user_id):
        user = self._users_by_id.get(to_user_id)
        if not user:
            raise ValueError("User not found")
        user.approve_friend_request(from_user_id)

    def reject_friend_request(self, from_user_id, to_user_id):
        user = self._users_by_id.get(to_user_id)
        if not user:
            raise ValueError("User not found")
        user.reject_friend_request(from_user_id)
