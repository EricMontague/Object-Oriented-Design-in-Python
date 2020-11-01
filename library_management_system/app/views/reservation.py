class ReservationView:
    @staticmethod
    def wants_to_reserve_book(book_title):
        answer = input(f"Would you like to reserve a copy of {book_title}? (y/n)")
        positive_answers = {"yes", "y", "1"}
        if answer.lower() in positive_answers:
            return True
        return False
