from app.services.book_service import book_service
from app.services.fine_service import fine_service
from app.services.reservation_service import reservation_service
from app.services.search_service import search_service


# Just to show that the imports work
def main():
    print(book_service)
    print(fine_service)
    print(reservation_service)
    print(search_service)


if __name__ == "__main__":
    main()
