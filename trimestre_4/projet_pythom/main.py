import tkinter as tk
from tkinter import messagebox
import model  # Import du fichier contenant les fonctions d'accès à la BD

def refresh_concerts():
    """Rafraîchit l'affichage des concerts."""
    for widget in frame.winfo_children():
        widget.destroy()  # Supprime tous les widgets pour recréer la liste
    
    concerts = model.read_table("concerts")  # Récupère les concerts depuis la BD
    
    if not concerts:
        tk.Label(frame, text="Aucun concert trouvé.", font=("Arial", 12)).pack()
        return

    for concert in concerts:
        concert_id = concert["id"]
        concert_name = concert["name"]
        concert_date = concert["datetime"]

        row_frame = tk.Frame(frame)
        row_frame.pack(fill="x", padx=5, pady=2)

        tk.Label(row_frame, text=f"{concert_id}: {concert_name} - {concert_date}", font=("Arial", 12)).pack(side="left", padx=5)
        
        btn_delete = tk.Button(row_frame, text="Delete", command=lambda cid=concert_id: delete_concert(cid), bg="red", fg="white")
        btn_delete.pack(side="right", padx=5)

def delete_concert(concert_id):
    """Supprime un concert après confirmation."""
    if messagebox.askyesno("Confirmation", f"Supprimer le concert ID {concert_id} ?"):
        model.delete_row("concerts", {"id": concert_id})
        refresh_concerts()  # Met à jour l'affichage

def add_concert():
    """Ajoute un concert à la base de données."""
    name = entry_name.get().strip()
    date_time = entry_datetime.get().strip()

    if not name or not date_time:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs !")
        return

    success = model.insert_row("concerts", {"name": name, "datetime": date_time})
    if success:
        messagebox.showinfo("Succès", "Concert ajouté avec succès !")
        entry_name.delete(0, tk.END)
        entry_datetime.delete(0, tk.END)
        refresh_concerts()  # Met à jour l'affichage
    else:
        messagebox.showerror("Erreur", "Impossible d'ajouter le concert.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Concerts Manager")
root.geometry("500x500")

# Bouton de rafraîchissement
btn_refresh = tk.Button(root, text="Refresh", command=refresh_concerts, bg="blue", fg="white")
btn_refresh.pack(pady=5)

# Frame pour afficher les concerts
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Formulaire d'ajout en bas
form_frame = tk.Frame(root, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Nom:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=2)
entry_name = tk.Entry(form_frame, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=2)

tk.Label(form_frame, text="Date/Heure:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=2)
entry_datetime = tk.Entry(form_frame, font=("Arial", 12))
entry_datetime.grid(row=1, column=1, padx=5, pady=2)

btn_add = tk.Button(form_frame, text="Ajouter", command=add_concert, bg="green", fg="white")
btn_add.grid(row=2, columnspan=2, pady=5)

# Chargement initial des concerts
refresh_concerts()

# Lancer l'application
root.mainloop()