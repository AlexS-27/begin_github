#Pour récupérer la clé privée stockée dans le keystore de geth
import json
from eth_account import Account

# Chemin vers le fichier keystore JSON
keystore_file = "c:/Users/pg11cvh/AppData/Local/Ethereum/keystore/UTCxxxxxxxxxxxxxxxxxxxxxx"

# Charger le fichier JSON
with open(keystore_file, "r") as f:
    encrypted_key = json.load(f)

# Mot de passe pour décrypter la clé
password = "xxxxxxxxxxxxxxxxxxxxxx"

# Décrypter la clé privée
private_key = Account.decrypt(encrypted_key, password)
print("Clé privée :", private_key.hex())
