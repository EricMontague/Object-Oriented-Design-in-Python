from app.services import search_service
from app.common import IObserver
from app.enums import Permissions


class User(IObserver):

    MAX_CHECKOUT_LIMIT = 5

    def __init__(self, user_id, name, password_hash, member_card):
        self._user_id = user_id
        self._name = name
        self._password_hash = password_hash
        self._member_card = member_card
        self._checked_out_books_by_book_id = {}
        self._reserved_books_by_book_id = {}
        self._permissions = set()
        self._permissions.add(Permissions.READ_BOOK)

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def permission(self):
        return list(self._permissions)

    def search(self, criteria, query):
        return search_service.search(criteria, query)

    def has_permissions(self, permission):
        return permission in self._permissions

    def add_permissions(self, permission):
        if self.has_permissions(permission):
            raise ValueError("User already has this permission")
        self._permissions.add(permission)

    def remove_permission(self, permission):
        if not self.has_permissions(permission):
            raise ValueError("User does not have this permission")
        self._permissions.remove(permission)

    def can_checkout(self):
        return len(self._checked_out_books_by_book_id) < self.MAX_CHECKOUT_LIMIT

    def is_member(self):
        return self._member_card is not None

    def add_member_card(self, member_card):
        if self.is_member():
            raise ValueError("User is already a member")
        self._member_card = member_card

    def has_overdue_book(self, book_id):
        for book_id in self._checked_out_books_by_book_id:
            book = self._checked_out_books_by_book_id[book_id]
            if book.is_overdue():
                return True
        return False

    def has_checked_out_book(self, book):
        return book.book_id in self._checked_out_books_by_book_id

    def has_reserved_book(self, book):
        return book.book_id in self._reserved_books_by_book_id

    def checkout(self, book):
        if not self.has_permissions(Permissions.CHECKOUT):
            raise ValueError("User does not have checkout permissions")
        if self.has_checked_out_book(book):
            raise ValueError("User has already checked out this book")
        if self.has_reserved_book(book):
            self._reserved_books_by_book_id.pop(book.book_id)
        self._checked_out_books_by_book_id[book.book_id] = book

    def reserve_book(self, book):
        if not self.has_permissions(Permissions.RESERVE):
            raise ValueError("User does not have book reservation permissions")
        if self.has_reserved_book(book):
            raise ValueError("User has already reserved this book")
        if self.has_checked_out_book(book):
            raise ValueError("User has this book checked out already")
        self._reserved_books_by_book_id[book.book_id] = book

    def return_book(self, book):
        if not self.has_permissions(Permissions.CHECKOUT):
            raise ValueError("User does not have checkout permissions")
        if self.has_checked_out_book(book):
            raise ValueError("The user has not checked out this book")
        self._checked_out_books_by_book_id.pop(book.book_id)

