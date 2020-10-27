from app.models.user import User
from app.service import book_service
from app.enums import Permissions

class Librarian(User):

    def __init__(self, user_id, name, password_hash, member_card):
        super().__init__(user_id, name, password_hash, member_card)
        for permission in Permissions:
            if not self.has_permissions(permission):
                self.add_permissions(permission)

    def add_book(self, book):
        book_service.add_book(book)

    def update_book(self, book_id, payload):
        book_service.update_book(book_id, payload)

    def remove_book(self, book_id):
        book_service.remove_book(book_id)
