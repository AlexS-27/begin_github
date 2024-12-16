from random import choice

from ICT114.ICT_114_PYTHON.Hashage_package.HashRequest import HashRequest

choice_manually = 'manuel'
choice_auto = 'auto'

def get_and_validate_user_choice():
    """
    Demande et valide le choix de l'utilisateur
    """
    user_input = input(
        "Voulez-vous entrer vos 14 chiffres ou générer un numéro aléatoire ? "
        f"(entrez '{choice_manually}' ou '{choice_auto}') : "
    ).strip().lower()
    if user_input not in [choice_manually, choice_auto]:
        print("Choix invalide. Veuillez réessayer.")
        return get_and_validate_user_choice()
    return user_input

def display_result(user_input ,result):

    if isinstance(result, tuple):
        complete_card = f"{user_input}{result[0]}{result[1]}"
        print(f"Les deux derniers chiffres pour rendre le numéro valide sont : {result[0]}{result[1]}")
        print(f"Numéro complet : {complete_card}")
    else:
        print(result)

def run_program(user_input=None):
    """
    Programme de génération au Luhn
    """
    HashRequest.get_user_input = user_input
    print("Bienvenue dans le générateur de numéros conformes à Luhn !")

    user_choice = get_and_validate_user_choice()
    result = HashRequest.get_last_digit(user_input)

    display_result(user_input, result)

if __name__ == "__main__":
    run_program()
