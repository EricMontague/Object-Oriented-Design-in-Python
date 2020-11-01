from uuid import uuid4
from app.models import Reservation


class _ReservationService:
    def __init__(self):
        self._reservations_by_book_id = {}

    def reserve_book(self, book, member):
        if self.has_reserved_book(book.book_id, member):
            raise ValueError("User has already reserved this book")
        new_reservation = Reservation(uuid4(), book, member)
        if book.book_id not in self._reservations_by_book_id:
            self._reservations_by_book_id[book.book_id] = []
        self._reservations_by_book_id[book.book_id].append(new_reservation)

    def unreserve_book(self, book_id, member):
        if book_id not in self._reservations_by_book_id:
            raise ValueError("There are no reservations for this book")
        reservations = self._reservations_by_book_id[book_id]
        for index in range(len(reservations)):
            if reservations[index].member == member:
                del reservations[index]
                break
        raise ValueError("User does not have a reservation for this book")

    def has_reserved_book(self, book_id, member):
        if book_id not in self._reservations_by_book_id:
            return False
        reservations = self._reservations_by_book_id[book_id]
        for reservation in reservations:
            if reservation.member == member:
                return True
        return False

    def get_reservations_by_book_id(self, book_id):
        if book_id not in self._reservations_by_book_id:
            raise ValueError("There are no reservations for this book")
        return self._reservations_by_book_id[book_id]


reservation_service = _ReservationService()
