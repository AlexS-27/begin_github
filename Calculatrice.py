def ask_number(message):
    while True:
        try:
            chiffre = float(input(message))
            return chiffre
        except ValueError:
            print("Erreur : Veuillez entrez un nombre")

chiffre1=ask_number("Donnez-moi un premier chiffre : ")
chiffre2=ask_number("Donnez-moi un deuxième chiffre : ")
symbole= input("Dites moi si vous désirez ; une addition, une soustraction, une multiplication ou une division : " )

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