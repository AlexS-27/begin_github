import hashlib

# Fonction pour hacher un fichier en SHA-256
def hash_pdf(file_path):
    # Créer un objet SHA-256
    sha256_hash = hashlib.sha256()

    try:
        # Ouvrir le fichier en mode binaire
        with open(file_path, "rb") as f:
            # Lire et mettre à jour le hash par petits morceaux
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        # Retourner le hash sous forme hexadécimale
        return sha256_hash.hexdigest()

    except FileNotFoundError:
        return f"Le fichier {file_path} n'a pas été trouvé."

# Exemple d'utilisation
file_path = "Hello.pdf"  # Remplacer par le chemin de votre fichier PDF
hash_result = hash_pdf(file_path)
print(f"Le hash SHA-256 du fichier est : {hash_result}")
