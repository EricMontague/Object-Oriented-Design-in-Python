class Fine:
    def __init__(self, fine_id, amount, book, member):
        self._fine_id = fine_id
        self._amount = amount
        self._member = member
        self._book = book
        self._paid = False

    def pay(self):
        self._paid = True

    def is_paid(self):
        return self._paid

    def increment(self, amount):
        self._amount += amount

    @property
    def fine_id(self):
        return self._fine_id

    @property
    def member(self):
        return self._member

    @property
    def amount_due(self):
        return self._amount

    @property
    def book(self):
        return self._book
