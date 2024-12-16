import random
from curses.ascii import isdigit

from ICT114.ICT_114_PYTHON.Hashage_package.HashRequest import HashRequest

class CardHash:
    # constante définissant la langueur du numéro de carte attendu
    card_length = 15

    def __init__(self):
        pass

    def isdigit(self):
        pass


    def validate_card_number(self):
        """
        vérifie si le numéro de carte est valide avec l'algorithme de Luhn.'
        """
        card_number = HashRequest.get_card_number
        return len(card_number) == self.card_length and \
        card_number.isdigit()

    def calculate_luhn_last_digit(self):
        """
        Calcule le dernier chiffre d'un numéro de carte
        de crédit pour rendre valide avec l'algorithme de Luhn.
        """
        """
        Étape 1 : Vérification de l'entrée
        """
        if not self.validate_card_number():
            return "Erreur: Entrez exactement 15 chiffres."
        """
        Étape 2 : Convertir la chaîne de caractères en une liste de chiffres
        """
        digits = [int(d) for d in self.card_number]  # Chaque caractère devient un chiffre entier
        """
        Étape 3 : Appliquer l'algorithme de Luhn sur les 15 chiffres
        """
        checksum =self.calculate_luhn_checksum(digits)
        """
        Étape 4 : Calculer le dernier chiffre (chiffre de contrôle)
        """
        # 1. Vérifie si le nombre est divisible par 10,2. Dit combien il manque pour faire 10 (donne le nombre manquant)3: vérifie que le nombre est compris entre 1-9.
        last_digit = (10 - (checksum % 10)) % 10
        return HashRequest.get_last_digit(last_digit)

    @staticmethod
    def calculate_luhn_checksum(digits):
        """
        Applique l'algorithme de Luhn pour calculer le checksum.
        """
        checksum = 0    # Initialisation de la somme de contrôle
        for i, digit in enumerate(reversed(digits)):  # On parcourt les chiffres de droite à gauche
            if i % 2 == 0:  # Les positions paires (en partant de la droite)
                digit *= 2  # Doubler le chiffre
                if digit > 9:  # Si le double est supérieur à 9
                    digit -= 9  # soustraire 9
            checksum += digit # Ajouter le chiffre transformé ou brut à la somme de contrôle
        return checksum

class CardSelector:
    card_length = CardHash.card_length

    def __init__(self):
        pass

    @staticmethod
    def generate_random_card_number(length=card_length):
        """
        Génère les 14 premiers chiffres d'un numéro de carte aléatoire.
        """
        return ''.join(str(random.randint(0, 9)) for _
        in range(length))

    def get_card_number_input(self):

        choice = HashRequest.get_user_input
        if choice == 'manuel':
            HashRequest.get_card_number = input("Entrez les 14 premiers chiffres de"
            "votre numéro de carte de crédit : ")
            return HashRequest.get_card_number
        elif choice == 'auto':
            HashRequest.get_card_number =\
                self.generate_random_card_number()
            print(f"Numéro aléatoire généré : {HashRequest.get_card_number}")
            return HashRequest.get_card_number

        else:
            print("Choix invalide. Veuillez réessayer.")
            return None
