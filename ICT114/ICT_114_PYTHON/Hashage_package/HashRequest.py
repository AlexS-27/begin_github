class HashRequest:
    def __init__(self, user_input, choice, card_number,
    last_digit):
        self.user_input = user_input
        self.choice = choice
        self.card_number = card_number
        self.last_digit = last_digit

    def get_user_input(self):
        return self.user_input

    def get_choice(self):
        return self.choice

    def get_card_number(self):
        return self.card_number

    def get_last_digit(self):
        return self.last_digit