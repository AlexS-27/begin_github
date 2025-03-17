import hashlib
import json
from web3 import Web3

# Chemin du fichier PDF
pdf_file = r"N:\Commun\ELEVE\INFO\SI-CA1a\Personnel\Alex\hello.alex.pdf"

# Lire le fichier PDF et calculer son hash SHA-256
with open(pdf_file, "rb") as f:
    pdf_data = f.read()

hash_pdf = hashlib.sha256(pdf_data).hexdigest()
print(f"Hash du fichier : {hash_pdf}")

# Créer les métadonnées
metadata = {
    "name": pdf_file,
    "hash": hash_pdf,
    "path": "Nom eleve",
    "description": "Exemple de fichier PDF"
}

# Convertir le dictionnaire en chaîne JSON
metadata_json = json.dumps(metadata)

# Convertir la chaîne JSON en dictionnaire Python (ceci n'est pas nécessaire dans ce cas, mais pour démonstration)
metadata_test = json.loads(metadata_json)

# Afficher les métadonnées
print("\nMétadonnées :")
print(f"Nom : {metadata_test.get('name', 'N/A')}")
print(f"Hash : {metadata_test.get('hash', 'N/A')}")
print(f"Chemin : {metadata_test.get('path', 'N/A')}")
print(f"Description : {metadata_test.get('description', 'N/A')}")

print(f"Données décodées (utf-8) : {metadata_json}")

# Convertir les métadonnées en JSON et ensuite en hexadécimal
metadata_hex = json.dumps(metadata).encode('utf-8').hex()
print(f"Métadonnées en hexadécimal : {metadata_hex}")

# Connexion au nœud Ethereum (Geth)
w3 = Web3(Web3.HTTPProvider('http://10.229.43.181:8545/'))  # Assurez-vous que le nœud est accessible

# Vérifier la connexion au nœud Ethereum
if not w3.is_connected():
    print("Impossible de se connecter au nœud Ethereum.")
    exit()
else:
    print("Connecté au nœud Ethereum.")

# Adresse et clé privée
from_account = "0xfadjfapsdfjpa"
to_account = "0x0000000000000000000000000000000000000000"
private_key = "la clé privée"  # Remplacez par la clé privée correspondante

# Convertir les adresses en format checksum
sender_address = w3.to_checksum_address(from_account)
recipient_address = w3.to_checksum_address(to_account)

# Récupérer le nonce pour l'adresse de l'expéditeur
nonce = w3.eth.get_transaction_count(sender_address)

# Création de la transaction
transaction = {
    'from': sender_address,
    'to': recipient_address,  # Adresse nulle
    'value': 0,  # Pas de transfert d'Ether
    'gas': 200000,  # Limite de gas
    'gasPrice': w3.to_wei('20', 'gwei'),  # Prix du gas
    'nonce': nonce,
    'chainId': 32382,  # Remplacez par votre chainId personnalisé
    'data': metadata_hex  # Champ contenant les métadonnées
}

# Afficher le contenu du champ 'data' avant d'envoyer la transaction
print(f"Contenu du champ 'data' : {transaction['data']}")

try:
    # Signer la transaction
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)

    # Envoyer la transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # Afficher le hash de la transaction
    print(f"Transaction envoyée avec succès ! Hash : {w3.to_hex(tx_hash)}")

except Exception as e:
    print(f"Une erreur est survenue lors de l'envoi de la transaction : {str(e)}")