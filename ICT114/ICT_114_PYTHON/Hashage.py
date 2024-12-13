def calculate_luhn_last_digit(card_number):
    """
    Calcule le dernier chiffre d'un numéro de carte de crédit pour rendre valide avec l'algorithme de Luhn.
    """
    # Étape 1 : Vérification de l'entrée
    if len(card_number) != 15 or not card_number.isdigit():
        return "Erreur: Entrez exactement 15 chiffres."
    # Étape 2 : Convertir la chaîne de caractères en une liste de chiffres
    digits = [int(d) for d in card_number]  # Chaque caractère devient un chiffre entier
    checksum = 0 # Initialisation de la somme de contrôle

    # Étape 3 : Appliquer l'algorithme de Luhn sur les 15 chiffres
    for i, digit in enumerate(reversed(digits)):    # On parcourt les chiffres de droite à gauche
        if i % 2 == 0:  # Les positions paires (en partant de la droite)
            digit *= 2  # Doubler le chiffre
            if digit > 9:    # Si le double est supérieur à 9
                digit -= 9  # soustraire 9
        checksum += digit    # Ajouter le chiffre transformé ou brut à la somme de contrôle

    # Étape 4 : Calculer le dernier chiffre (chiffre de contrôle)
    last_digit = (10 - (checksum % 10)) % 10 #1. Vérifie si le nombre est divisible par 10,2. Dit combien il manque pour faire 10 (donne le nombre manquant)3: vérifie que le nombre est compris entre 1-9.
    return last_digit

# Exemple d'utilisation
if __name__ == "__main__":
    user_input = input("Entrez les 15 premiers chiffres de votre numéro de carte de crédit : ")
    result = calculate_luhn_last_digit(user_input)
    if isinstance(result, int):
        print(f"Le dernier chiffre pour rendre le numéro valide est : {result}")
        print(f"Numéro complet : {user_input}{result}")
    else:
        print(result)
