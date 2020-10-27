from datetime import datetime, timedelta


class MemberCard:

    MEMBERSHIP_LENGTH_IN_WEEKS = 52 * 3

    def __init__(self, barcode, member):
        self._barcode = barcode
        self._member = member
        self._issued_on_date = datetime.now()
        self._expires_on_date = timedelta(self._issued_on_date) + timedelta(
            weeks=self.MEMBERSHIP_LENGTH_IN_WEEKS
        )

    def is_expired(self):
        return datetime.now() > self._expires_on_date

    def renew(self):
        self._issued_on_date = datetime.now()
        self._expires_on_date = timedelta(self._issued_on_date) + timedelta(
            weeks=self.MEMBERSHIP_LENGTH_IN_WEEKS
        )

    @property
    def expires_on_date(self):
        return self._expires_on_date

    @property
    def issued_on_date(self):
        return self._issued_on_date

    @property
    def member(self):
        return self._member

    @property
    def barcode(self):
        return self._barcode
