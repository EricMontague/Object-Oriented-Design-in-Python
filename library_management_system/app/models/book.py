from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author, subject, publication_date, rack_number):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._subject = subject
        self._publication_date = publication_date
        self._rack_number = rack_number
        self._copies = []

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def subject(self):
        return self._subject

    @property
    def publication_date(self):
        return self._publication_date

    @property
    def copies(self):
        return self._copies

    @property
    def rack_number(self):
        return self._rack_number

    def is_available(self):
        for copy in self._copies:
            if copy.is_checked_out():
                return True
        return False

    def num_copies_available(self):
        num_copies_available = 0
        for copy in self._copies:
            if copy.is_checked_out():
                num_copies_available += 1
        return num_copies_available

    def checkout_book(self):
        for copy in self._copies:
            if copy.is_checked_out():
                copy.checkout_copy()
                return copy
        return None

    def return_book(self):
        for copy in self._copies:
            if not copy.is_checked_out():
                copy.return_copy()
                return True
        return False


class BookCopy:

    CHECKOUT_LENGTH_IN_WEEKS = 4

    def __init__(self, barcode):
        self._checked_out_on_date = None
        self._due_date = None
        self._barcode = barcode

    @property
    def checked_out_on_date(self):
        return self._checked_out_on_date

    @property
    def barcode(self):
        return self._barcode

    def checkout_copy(self):
        if self.is_checked_out():
            raise ValueError("Copy is already checked out")
        self._checked_out_on_date = datetime.now()
        self._due_date = (
            timedelta(self._checked_out_on_date) 
            + timedelta(weeks=self.CHECKOUT_LENGTH_IN_WEEKS)
        )

    def return_copy(self):
        if not self.is_checked_out():
            raise ValueError("Copy is not currently checked out")
        self._checked_out_on_date = None
        self._due_date = None

    def is_checked_out(self):
        return self._checked_out_on_date is not None

    def is_overdue(self):
        return datetime.now() > self._due_date

    def due_date(self):
        return self._due_date

