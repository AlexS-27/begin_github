def ajouter_objet(bit):
    global inventaire
    inventaire |= bit
    print("object add")

inventaire= 0xA2
objet = ("cuilliere", "fourchette", "couteau", "gamelle", "lampe", "pince", "tournevis", "marteau", )

def retirer_objet(bit):
    global inventaire
    inventaire &= ~bit
    print("object remove")

#déclaration des constante pour le bitfield
cuilliere = 0b00000001
fourchette = 0b00000010
couteau = 0b00000100
gamelle = 0b00001000
lampe = 0b00010000
pince = 0b00100000
tournevis = 0b01000000
marteau = 0b10000000

def afficher_inventaire():
    global inventaire
    print("actual inventory")
    for i, nom in enumerate(objet):
        if inventaire & (1 << i):
            print(f"- {nom}")

def afficher_menu():
    print("Menu")
    print("1. Afficcher le menu")
    print(f"2. ajouter cuilliere")
    print("3. retirer cuilliere")
    print("4. ajouter fourchette")
    print("5. retirer fourchette")
    print("6. ajouter couteau")
    print("7. retirer couteau")
    print("8. ajouter gamelle")
    print("9. retirer gamelle")
    print("10. ajouter lampe")
    print("11. retirer lampe")
    print("12. ajouter pince")
    print("13. retirer pince")
    print("14. ajouter tournevis")
    print("15. retirer tournevis")
    print("16. ajouter marteau")
    print("17. retirer marteau")
    print("18. Quitter")

def add_remove():
    while True:
        afficher_menu()
        choix = input("Quelle action désirez-vous faire ? : ")

        if choix == "1":
            afficher_inventaire()

        elif choix == "2":
            ajouter_objet(cuilliere)
        elif choix == "3":
            retirer_objet(cuilliere)

        elif choix == "4":
            ajouter_objet(fourchette)
        elif choix == "5":
            retirer_objet(fourchette)

        elif choix == "6":
            ajouter_objet(couteau)
        elif choix == "7":
            retirer_objet(couteau)

        elif choix == "8":
            ajouter_objet(gamelle)
        elif choix == "9":
            retirer_objet(gamelle)

        elif choix == "10":
            ajouter_objet(lampe)
        elif choix == "11":
            retirer_objet(lampe)

        elif choix == "12":
            ajouter_objet(pince)
        elif choix == "13":
            retirer_objet(pince)

        elif choix == "14":
            ajouter_objet(tournevis)
        elif choix == "15":
            retirer_objet(tournevis)

        elif choix == "16":
            ajouter_objet(marteau)
        elif choix == "17":
            retirer_objet(marteau)
        elif choix == "18":
            print("Bye")
            break

        else:
            print("The number isn't in list please try again")