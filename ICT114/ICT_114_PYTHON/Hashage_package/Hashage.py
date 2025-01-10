from random import choice

from ICT114.ICT_114_PYTHON.Hashage_package.HashRequest import HashRequest
from ICT114.ICT_114_PYTHON.Hashage_package.HashLib import CardHash, CardSelector

choice_manually = 'manuel'
choice_auto = 'auto'

def get_and_validate_user_choice():
    """
    Demande et valide le choix de l'utilisateur
    """
    while True:
        user_input = input(
            "Voulez-vous entrer vos 14 chiffres ou générer un numéro aléatoire ? "
            f"(entrez '{choice_manually}' ou '{choice_auto}') : "
        ).strip().lower()
        if user_input in [choice_manually, choice_auto]:
            return user_input
        else:
            print("Choix invalide. Veuillez réessayer.")

def display_result(user_input ,result):

    if isinstance(result, tuple):
        complete_card = f"{user_input}{result[0]}{result[1]}"
        print(f"Les deux derniers chiffres pour rendre le numéro valide sont : {result[0]}{result[1]}")
        print(f"Numéro complet : {complete_card}")
    else:
        print(result)

def get_card_number_input(user_choice):

    if user_choice == 'manuel':
        user_input = input("Entrez les 14 premiers chiffres de"
        "votre numéro de carte de crédit : ")
        return user_input
    elif user_choice == 'auto':
        user_input = CardSelector.generate_random_card_number()
        print(f"Numéro aléatoire généré : {user_input}")
        return user_input

    else:
        print("Choix invalide. Veuillez réessayer.")
        return None

def run_program():
    """
    Programme de génération au Luhn
    """
    print("Bienvenue dans le générateur de numéros conformes à Luhn !")

    user_choice = get_and_validate_user_choice()


    user_input = get_card_number_input(user_choice)

    hash_request = HashRequest(
        user_input=user_input,
        choice=user_choice)

    result = hash_request.get_last_digit(2)

    display_result(user_input, result)

if __name__ == "__main__":
    run_program()
