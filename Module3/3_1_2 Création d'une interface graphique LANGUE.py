# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.1.2 Création d'une interface graphique
# Description : Interface Graphique pratique autonome
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions
def cliqueAnglais():
    lblMot ['text'] = "Hello"

def cliqueFrancais():
    lblMot ['text'] = "Bonjour"
    

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Mon école")
fenetre.geometry("400x300")
fenetre.configure(bg = "#ffffff")

# - Anglais
btnAnglais = tk.Button(fenetre)
btnAnglais ['text'] = "Anglais"
btnAnglais ['font'] = ["Arial", 20]
btnAnglais ['command'] = cliqueAnglais()
btnAnglais.pack()

# - Anglais
btnFrancais = tk.Button(fenetre)
btnFrancais ['text'] = "Francais"
btnFrancais ['font'] = ["Arial", 20]
btnFrancais ['command'] = cliqueFrancais()
btnFrancais.pack()




fenetre.mainloop()