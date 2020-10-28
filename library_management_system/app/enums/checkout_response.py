from enum import Enum


class CheckoutResponse(Enum):

    USER_REFUSED_TO_PAY_FINE = 0
    USER_PAID_FINE = 1
    USER_REFUSED_TO_RESERVE_BOOK = 2
    USER_RESERVED_BOOK = 3
    USER_CHECKED_OUT_BOOK = 4