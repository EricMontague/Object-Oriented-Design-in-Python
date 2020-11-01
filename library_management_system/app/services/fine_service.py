from app.models import Fine
from uuid import uuid4


class _FineService:

    _FINE_PER_DAY_IN_CENTS = 25

    def __init__(self):
        self._fines_by_member_id = {}

    def get_amount_due(self, member_id):
        fines = self._fines_by_member_id.get(member_id, [])
        if not fines:
            raise ValueError("User does not currently have any outstanding fines.")
        amount = 0
        for fine in fines:
            amount += fine.amount_due
        return amount

    def create_fine(self, book, member, amount=0):
        fine_amount = amount or self._FINE_PER_DAY_IN_CENTS
        fine = Fine(uuid4(), fine_amount, book, member)
        if not self.owes_money(member.user_id):
            self._fines_by_member_id[member.user_id] = []
        self._fines_by_member_id[member.user_id].append(fine)

    def increment_fine(self, book, member, amount=0):
        if not self.owes_money(member.user_id):
            raise ValueError("User does not currently have any outstanding fines")
        increment_amount = amount or self._FINE_PER_DAY_IN_CENTS
        fines = self._fines_by_member_id[member.user_id]
        for fine in fines:
            if fine.book == book:
                fine.increment(increment_amount)
                break

    def owes_money(self, member_id):
        if not member_id in self._fines_by_member_id:
            return False
        fines = self._fines_by_member_id[member_id]
        for fine in fines:
            if not fine.is_paid():
                return True
        return False

    def owes_money_for_book(self, book, member):
        if not member.user_id in self._fines_by_member_id:
            return False
        fines = self._fines_by_member_id[member.user_id]
        for fine in fines:
            if fine.book == book and not fine.is_paid():
                return True
        return False

    def charge(self, amount, book, member):
        if not self.owes_money(member.user_id):
            raise ValueError("User does not currently have any outstanding fines")
        fines = self._fines_by_member_id[member.user_id]
        for fine in fines:
            if fine.book == book:
                fine.pay()
                break

    def get_fine_per_day(self):
        return self._FINE_PER_DAY_IN_CENTS


fine_service = _FineService()
