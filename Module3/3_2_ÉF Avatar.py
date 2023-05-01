# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.2.ÉF Avatar
# Description : Interface graphique permettant l'utilisateur de créer un avatar
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions
def cliqueBilan():
    lblBilan['text'] = "Vous avez sélectionné \ndes cheveux " + cheveux.get() + " et " + couleur.get() + "."

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Création d'un avatar")
fenetre.geometry("600x350")
fenetre.configure(bg = "#ffffff")

# - Titre pour l'interface

lblTitre = tk.Label(fenetre)
lblTitre['text'] = "Création d'un avatar"
lblTitre['font'] = ["Arial", 30, "bold"]
lblTitre['bg'] = "#ffffff"
lblTitre.grid(row=0,column=0,columnspan=2, padx=100)

# - Titre pour options de cheveux

lblCheveux = tk.Label(fenetre)
lblCheveux['text'] = "Options de Cheveux"
lblCheveux['font'] = ["Arial", 15, "bold"]
lblCheveux['bg'] = "#ffffff"
lblCheveux.grid(row=1,column=0)

# - Choix de cheveux
cheveux = tk.StringVar()

# - Cheveux longs
radLongs = tk.Radiobutton(fenetre)
radLongs['text'] = "Longs"
radLongs['font'] = ["Arial", 15]
radLongs['bg'] = "#ffffff"
radLongs['value'] = "longs"
radLongs['variable'] = cheveux
radLongs.select()
radLongs.grid(row=2,column=0)

# - Cheveux chauve
radChauve = tk.Radiobutton(fenetre)
radChauve['text'] = "Chauve"
radChauve['font'] = ["Arial", 15]
radChauve['bg'] = "#ffffff"
radChauve['value'] = "chauve"
radChauve['variable'] = cheveux
radChauve.grid(row=3,column=0)

# - Titre pour options de couleur de cheveux
lblCouleur = tk.Label(fenetre)
lblCouleur['text'] = "Options de couleur"
lblCouleur['font'] = ["Arial", 15, "bold"]
lblCouleur['bg'] = "#ffffff"
lblCouleur.grid(row=4,column=0)

# - Choix de couleur
couleur = tk.StringVar()

# - Cheveux bruns
radBrun = tk.Radiobutton(fenetre)
radBrun['text'] = "Brun"
radBrun['font'] = ["Arial", 15]
radBrun['bg'] = "#ffffff"
radBrun['value'] = "bruns"
radBrun['variable'] = couleur
radBrun.select()
radBrun.grid(row=5,column=0)

# - Cheveux blonds
radBlond = tk.Radiobutton(fenetre)
radBlond['text'] = "Blond"
radBlond['font'] = ["Arial", 15]
radBlond['bg'] = "#ffffff"
radBlond['value'] = "blonds"
radBlond['variable'] = couleur
radBlond.grid(row=6,column=0)

# - Resultat
lblResultat = tk.Label(fenetre)
lblResultat['text'] = "Bilan de vos sélections seront ici"
lblResultat['font'] = ["Arial", 15, "bold"]
lblResultat['bg'] = "#ffffff"
lblResultat.grid(row=1,column=1)

# - Bilan
lblBilan = tk.Label(fenetre)
lblBilan['text'] = ""
lblBilan['font'] = ["Arial", 15]
lblBilan['bg'] = "#ffffff"
lblBilan.grid(row=2,column=1)

# - Bouton
btnBilan = tk.Button(fenetre)
btnBilan['text'] = "Passer au bilan"
btnBilan['font'] = ["Arial", 15]
btnBilan['bg'] = "#ffffff"
btnBilan['command'] = cliqueBilan
btnBilan.grid(row=7,column=0)

# - Étape suivante
btnSuivant = tk.Button(fenetre)
btnSuivant['text'] = "Étape suivante"
btnSuivant['font'] = ["Arial", 15]
btnSuivant['bg'] = "#ffffff"
btnSuivant.grid(row=7,column=1)

fenetre.mainloop()
