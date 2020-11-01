from datetime import datetime


class Reservation:
    def __init__(self, reservation_id, book, member):
        self._reservation_id = reservation_id
        self._book = book
        self._member = member
        self._reserved_on_date = datetime.now()

    @property
    def reservation_id(self):
        return self._reservation_id

    @property
    def book(self):
        return self._book

    @property
    def member(self):
        return self._member

    @property
    def reserved_on_date(self):
        return self._reserved_on_date
