import base64
import os

# Afficher le répertoire courant
print(f"Le fichier sera sauvegardé dans : {os.getcwd()}")

# Demander à l'utilisateur de fournir une chaîne encodée en base64
encoded_string = input("Mettez votre chaîne à décoder : ")

# Décoder la chaîne base64 en octets
decoded_bytes = base64.b64decode(encoded_string)

try:
    # Tentative de décodage en UTF-8 pour vérifier si c'est du texte
    decoded_string = decoded_bytes.decode("utf-8")
    print(f"Chaîne décodée en texte : {decoded_string}")
except UnicodeDecodeError:
    # Si l'échec du décodage en UTF-8, traiter comme données binaires
    print("Les données sont des données binaires. Sauvegarde dans un fichier.")
    # Sauvegarder les octets dans un fichier (par exemple, une image PNG)
    with open("output_image.png", "wb") as file:
        file.write(decoded_bytes)
    print("Données binaires enregistrées dans 'output_image.png'")
