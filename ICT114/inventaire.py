from def_inventaire import *

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

add_remove()