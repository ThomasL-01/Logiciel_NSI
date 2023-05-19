import tkinter as tk

# Fonction appelée lorsque le bouton est cliqué
def afficher_message():
    message = entry.get()
    label.config(text=message)

# Création de la fenêtre principale
window = tk.Tk()

# Création des widgets
label = tk.Label(window, text="Texte initial du Label")
entry = tk.Entry(window)
button = tk.Button(window, text="Afficher", command=afficher_message)

# Positionnement des widgets avec grid()
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry.grid(row=1, column=0, padx=10, pady=10)
button.grid(row=1, column=1, padx=10, pady=10)

# Lancement de la boucle principale
window.mainloop()
