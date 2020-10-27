from app.models.user import AbstractUser
from app.common import IObserver


class Member(AbstractUser, IObserver):

    MAX_CHECKOUT_LIMIT = 5

    def __init__(self, user_id, name, password_hash, member_card):
        super().__init__(user_id, name, password_hash)
        self._member_card = member_card
        self._checked_out_books_by_book_id = {}
        self._reserved_books_by_book_id = {}

    def can_checkout(self):
        return len(self._checked_out_books_by_book_id) < self.MAX_CHECKOUT_LIMIT

    def is_member(self):
        return self._member_card is not None

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
        if self.has_checked_out_book(book):
            raise ValueError("Member has already checked out this book")
        if self.has_reserved_book(book):
            self._reserved_books_by_book_id.pop(book.book_id)
        self._checked_out_books_by_book_id[book.book_id] = book

    def reserve_book(self, book):
        if self.has_reserved_book(book):
            raise ValueError("Member has already reserved this book")
        if self.has_checked_out_book(book):
            raise ValueError("Member has this book checked out already")
        self._reserved_books_by_book_id[book.book_id] = book

    def return_book(self, book):
        if self.has_checked_out_book(book):
            raise ValueError("The member has not checked out this book")
        self._checked_out_books_by_book_id.pop(book.book_id)

