class HashRequest:
    def __init__(self, user_input, choice=None):
        self.user_input = user_input
        self.choice = choice
        self.card_number = user_input
        self.last_digit = None

    def get_user_input(self):
        return self.user_input

    def get_choice(self):
        return self.choice

    def get_card_number(self):
        return self.card_number

    def get_last_digit(self,digit_count):
        if not self.card_number or len(self.card_number) < digit_count:
            raise ValueError(f"Invalid card number must be at least 1{digit_count} digits long")
        self.last_digit = self.card_number[-digit_count:]
        return self.last_digit