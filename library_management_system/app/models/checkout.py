class Checkout:
    def __init__(self, member, book_copy):
        self._member = member
        self._book_copy = book_copy

    @property
    def member(self):
        return self._member

    @property
    def book_copy(self):
        return self._book_copy
