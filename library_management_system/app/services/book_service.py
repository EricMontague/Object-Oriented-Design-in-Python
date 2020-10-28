from app.services.fine_service import fine_service
from app.services.reservation_service import reservation_service
from app.views.user_interface import user_interface
from app.common.subject import ISubject
from app.enums import CheckoutResponse
from app.models import Checkout
from app.models import Notification


class BookService(ISubject):

    MAX_CHECKOUT_LIMIT = 5
    # _instance = None

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = object.__new__(cls)
    #     return cls._instance

    def __init__(self, books):
        self._books_by_id = books
        self._checked_out_books_by_user_id = {}

    def notify_observers(self, book_id):
        reservations = reservation_service.get_reservations_by_book_id(book_id)
        for reservation in reservations:
            message = f"The book titled {reservation.book.title} is now available"
            notificationn = Notification(message, reservation.member)
            reservation.member.receive_notification(notificationn)

    def add_observer(self, checkout):
        self._checked_out_books_by_user_id[checkout.member.user_id] = checkout

    def remove_observer(self, user_id):
        if not self.has_taken_out_book(user_id):
            raise ValueError("Observer not found")
        self._checked_out_books_by_user_id.pop(user_id)

    def get_book_rack_number(self, book_id):
        if not self.has_book_in_library(book_id):
            raise ValueError("Book not found")
        return self._books_by_id[book_id].rack_number

    def checkout_book(self, book_id, member):
        if not self.has_book_in_library(book_id):
            raise ValueError("Book not found")
        if member.has_overdue_book():
            amount = fine_service.get_amount_due(member.user_id)
            if not user_interface.wants_to_pay_fine(amount, member.name):
                return CheckoutResponse.USER_REFUSED_TO_PAY_FINE
            fine_service.charge(member, amount)
            return CheckoutResponse.USER_PAID_FINE

        if member.num_books_checked_out() == self.MAX_CHECKOUT_LIMIT:
            raise ValueError(
                f"User has reached the limit({self.MAX_CHECKOUT_LIMIT})"
                + "for the number books they can checkout at once"
            )

        book = self._books_by_id[book_id]
        # If book not available, ask user if they want to reservere copy
        if not book.is_avaiable():
            if not user_interface.wants_to_reserve_book(book.title):
                return CheckoutResponse.USER_REFUSED_TO_RESERVE_BOOK
            reservation_service.reserve_book(book_id, member)
            return CheckoutResponse.USER_RESERVED_BOOK
        # Need to look into barcode vs book id here
        # what happens if the member.checkout_book() method raises an error?
        # checkout book
        book_copy = book.checkout_book()
        member.checkout_book(book_copy)
        checkout = CheckoutResponse(book_copy, member)
        self.add_observer(checkout)

        # remove existing reservation if there is one
        if reservation_service.has_reserved_book(book_id, member):
            reservation_service.unreserve_book(book_id, member)
        return CheckoutResponse.USER_CHECKED_OUT_BOOK

    def return_book(self, book_id, member):
        if not self.has_book_in_library(book_id):
            raise ValueError("Book not found")
        if not self.has_taken_out_book(member.user_id):
            raise ValueError("User has not taken out this book")
        book = self._books_by_id[book_id]
        checkout = self._checked_out_books_by_user_id[member.user_id]
        if checkout.book_copy.is_overdue():
            amount = fine_service.get_amount_due(member.user_id)
            if user_interface.wants_to_pay_fine(amount):
                fine_service.charge(member, amount)
        book.return_book(checkout.book_copy)
        member.return_book(checkout.book_copy.barcode)
        self.remove_observer(member.user_id)
        # notify others that have reserved this book that it is available
        self.notify_observers()
        return True

    def has_book_in_library(self, book_id):
        return book_id in self._books_by_id

    def has_taken_out_book(self, user_id):
        return user_id in self._checked_out_books_by_user_id

    def book_taken_out_by(self, barcode):
        members = []
        for user_id in self._checked_out_books_by_user_id:
            checkout = self._checked_out_books_by_user_id[user_id]
            if checkout.book_copy.barcode == barcode:
                members.append(checkout.member)
        return members

