from Calculatrice import chiffre1, chiffre2

question = input("Entrez le calcul a effectuer (par exemple 1 + 1) : ")

try:
    chiffre1_str, symbole, chiffre2_str = [element.strip() for element in question.split()]

    chiffre1 = float(chiffre1_str)
    chiffre2 = float(chiffre2_str)

    liste_symbole=["addition", "soustraction", "multiplication", "division", "+", "-", "*", "/"]

    while symbole not in liste_symbole:
        print("Il me faut le nom ou le symbole de la fonction")
        symbole=input("Dites moi si vous désirez ; une addition, une soustraction, une multiplication ou une division : " )
        if symbole in liste_symbole:
            break

    if symbole == "addition" or symbole == "+":
        result=(chiffre1 + chiffre2)
    elif symbole == "soustraction" or symbole == "-":
        result=(chiffre1 - chiffre2)
    elif symbole == "multiplication" or symbole == "*":
        result=(chiffre1 * chiffre2)
    elif symbole == "division" or symbole == "/":
        if chiffre2 != 0:
            result=(chiffre1 / chiffre2)
        else:
            print("La division par 0 est impossible")

    print(f"Le résultat est {result}")

except ValueError:
    print("Erreur : Veuillez mettre les deux nombres et l'opération correctement, séparé d'un espace")
except IndexError:
    print("Erreur : Faites attention à se que les trois élément soit séparé d'un espace")