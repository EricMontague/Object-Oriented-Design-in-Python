class Fine:
    def __init__(self, fine_id, amount, member):
        self._fine_id = fine_id
        self._amount = amount
        self._member = member
        self._paid = False

    def pay(self):
        self._paid = True

    def is_paid(self):
        return self._paid

    @property
    def fine_id(self):
        return self._fine_id

    @property
    def member(self):
        return self._member
