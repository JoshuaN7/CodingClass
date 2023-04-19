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

def cliqueEspanol():
    lblMot ['text'] = "Hola"
    

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Langues Différentes")
fenetre.geometry("400x300")
fenetre.configure(bg = "#ffffff")

# - Anglais
btnAnglais = tk.Button(fenetre)
btnAnglais ['text'] = "Anglais"
btnAnglais ['font'] = ["Arial", 15]
btnAnglais ['command'] = cliqueAnglais
btnAnglais.pack()

# - Francais
btnFrancais = tk.Button(fenetre)
btnFrancais ['text'] = "Francais"
btnFrancais ['font'] = ["Arial", 15]
btnFrancais ['command'] = cliqueFrancais
btnFrancais.pack()

# - Espanol
btnEspanol = tk.Button(fenetre)
btnEspanol ['text'] = "Espanol"
btnEspanol ['font'] = ["Arial", 15]
btnEspanol ['command'] = cliqueEspanol
btnEspanol.pack()

# - Mot
lblMot = tk.Label(fenetre)
lblMot ['text'] = "Bonjour"
lblMot ['font'] = ["Arial", 30, "bold"]
lblMot ['bg'] = "#ffffff"
lblMot.pack()

fenetre.mainloop()
