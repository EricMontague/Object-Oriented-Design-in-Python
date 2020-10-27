from enum import Enum


class Permissions(Enum):

    CREATE_BOOK = 0
    READ_BOOK = 1
    UPDATE_BOOK = 2
    DELETE_BOOK = 3
    CHECKOUT = 4
    RESERVE = 5

