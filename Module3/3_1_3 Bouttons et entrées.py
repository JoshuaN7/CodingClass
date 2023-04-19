# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.1.3 Interface graphique avec bouttons et entrées
# Description : Interface graphique où tu dois devnier la bonne combinaison
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions
def btnVerifier():
    if reponse.get() == "Wawa":
        print("yay")

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Combinaison")
fenetre.geometry("400x300")
fenetre.configure(bg = "#ffffff")

# - Mot
lblMot = tk.Label(fenetre)
lblMot ['text'] = "Devine le mot"
lblMot ['font'] = ["Arial", 30, "bold"]
lblMot ['bg'] = "#ffffff"
lblMot.pack()

# - Boite de texte
reponse = tk.Entry(fenetre)
reponse ['width'] = 15
reponse ['font'] = ["Arial", 15]
reponse ['textvariable'] = reponse
reponse.pack()


fenetre.mainloop()
