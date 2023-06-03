# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 4.4 Jeu de cartes
# Description : Programme qui pige des cartes
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import random
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Paquet
paquet = []
for i in range(1, 53):
    paquet.append(i)


# - Fonctions

def carteTexte(carte):
    type = ""
    if carte <= 13:
        type = " pique"
    elif carte <= 26:
        type = " coeur"
        carte = carte - 13
    elif carte <= 39:
        type = "trèfle"
        carte = carte - 26
    else:
        type = "carreau"
        carte = carte - 39

    sortie = ""
    if carte == 1:
        sorite = "As de"
    elif carte == 11:
        sorite = "Valet de"
    elif carte == 12:
        sorite = "Dame de"
    elif carte == 13:
        sorite = "Roi de"
    else:
        sortie = str(carte) + " de "
    return sortie + type

def piger():
    nbCartes = len(paquet)

    if nbCartes>=1:
        cartePos = random.randint(0, nbCartes-1)
        carteHasard = paquet[cartePos]

        lblTexte['text'] = carteTexte(carteHasard)
        lblCarte['image'] = imgPaquet[carteHasard]
        paquet.pop(cartePos)
        print(paquet)
    else:
        lblTexte['text'] = 'Il n\'y a plus de cartes dans le paquet'
        btnPiger['state'] = tk.DISABLED


# - Fenetre
fenetre = tk.Tk()
fenetre.title("Jeu de cartes")
fenetre.geometry("500x500")

# - Images
imgPaquet = []
for i in range(0, 53):
    fichier = str(i) + ".gif"
    imgPaquet.append(tk.PhotoImage(file=fichier))

# - Bouton pour piger
btnPiger = tk.Button()
btnPiger['text'] = "Piger une carte"
btnPiger['bg'] = "#ffffff"
btnPiger['fg'] = "#000000"
btnPiger['font'] = "Arial 12"
btnPiger['command'] = piger
btnPiger.pack()

# - Image de carte
lblCarte = tk.Label()
lblCarte['image'] = imgPaquet[0]
lblCarte.pack()

# - Texte pour carte
lblTexte = tk.Label()
lblTexte['text'] = "Arrière de la carte" 
lblTexte['font'] = "Arial 12"
lblTexte.pack()

fenetre.mainloop()