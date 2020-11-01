class PaymentsView:
    @staticmethod
    def wants_to_pay_fine(amount):
        print(f"You currently owe the library {amount}")
        answer = input(f"Would you like to pay your fine now? (y/n)")
        positive_answers = {"yes", "y", "1"}
        if answer.lower() in positive_answers:
            return True
        return False
