
from tkinter.font import names
from operator import truediv, index

#déclaration des constante pour le bitfield
cuilliere = 0b00000001
fourchette = 0b00000010
couteau = 0b00000100
gamelle = 0b00001000
lampe = 0b00010000
pince = 0b00100000
tournevis = 0b01000000
marteau = 0b10000000

#création d'un tuple
objet = ("cuilliere", "fourchette", "couteau", "gamelle", "lampe", "pince", "tournevis", "marteau", )

#création d'un fonction pour transformer les valeur en bool
def comparaison (objet_choisis, bitfield):
    try:
        #Trouver l'indice de l'objet dans le tuple
        index = objet.index(objet_choisis)
        #Vérifier si le bit correspondant est allumé
        return (bitfield & (1 << index)) != 0
    except ValueError:
        #Objet pas trouver
        return False

#initialisation du bitfield
bitfield = 0b00000000

def afficher_inventaire():
    if objet & cuilliere:
        print(" -Cuilliere")
    if objet & fourchette:
        print(" -Fourchette")
    if objet & couteau:
        print(" -Couteau")
    if objet & gamelle:
        print(" -Gamelle")
        if objet & lampe:
        print(" -Lampe")
    if objet & pince:
        print(" -Pince")
    if objet & tournevis:
        print(" -Tournevis")
    if objet & marteau:
        print(" -Marteau")

def ajouter_couteau():
    global objet
    objet |= couteau
    print("Mis un couteau dans l'inventaire")


for i, nom in enumerate(objet):
    if (bitfield & (1 << i)) != 0:
        print(f"x - {nom}")
    else:
        print(f"o - {nom}")
