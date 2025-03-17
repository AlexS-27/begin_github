from web3 import Web3
import json

# Connexion au nœud Ethereum (Geth)
w3 = Web3(Web3.HTTPProvider('http://10.229.43.181:8545/'))  # Assurez-vous que le nœud est accessible

# Hash de la transaction que vous souhaitez lire
tx_hash = "0x1e714d0e2b43d326fd42995542657138cd80b4f2010c374f4d001c046f9dc4d3"  # Remplacez par le hash de la transaction que vous avez envoyée

try:
    # Récupérer la transaction
    tx = w3.eth.get_transaction(tx_hash)

    # Afficher les détails de la transaction
    print("Détails de la transaction :")
    print(f"Hash : {tx_hash}")
    print(f"De : {tx['from']}")
    print(f"À : {tx['to']}")
    print(f"Valeur : {tx['value']} wei")
    print(f"Gas : {tx['gas']}")
    print(f"Prix du gas : {tx['gasPrice']} wei")
    print(f"Nonce : {tx['nonce']}")
    print(f"Données : {tx['input']}")

    # Décoder les métadonnées à partir du champ 'input'
    metadata_hex = tx['input'].hex()[2:]  # Convertir HexBytes en str et supprimer le préfixe '0x'
    print(f"Données brutes (hex) : {metadata_hex}")

    try:
        # Convertir les données hexadécimales en bytes puis en str
        metadata_bytes = bytes.fromhex(metadata_hex)
        metadata_json = metadata_bytes.decode('utf-8')
        print(f"Données décodées (utf-8) : {metadata_json}")

        # Vérifiez si les données décodées sont au format JSON
        if metadata_json.startswith('{') and metadata_json.endswith('}'):
            metadata = json.loads(metadata_json)

            # Afficher les métadonnées
            print("\nMétadonnées :")
            print(f"Nom : {metadata.get('name', 'N/A')}")
            print(f"Hash : {metadata.get('hash', 'N/A')}")
            print(f"Chemin : {metadata.get('path', 'N/A')}")
            print(f"Description : {metadata.get('description', 'N/A')}")
        else:
            print("Erreur : Les données décodées ne sont pas au format JSON valide.")

    except json.JSONDecodeError:
        print("Erreur : Les données ne sont pas au format JSON valide.")
    except UnicodeDecodeError:
        print("Erreur : Les données ne peuvent pas être décodées en UTF-8.")
    except Exception as e:
        print(f"Erreur lors du décodage des métadonnées : {str(e)}")

except Exception as e:
    print(f"Une erreur est survenue : {str(e)}")