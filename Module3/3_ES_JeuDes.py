# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.ES.JeuDes
# Description : Interface graphique pour le jeu de dés crée dans 
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions

# - Fenetre
fenetre = tk.Tk()
fenetre.title("Jeu de dés")
fenetre.geometry("1000x500")
fenetre['bg'] = "#ffffff"

# - Création des cadres
cadreChoix = tk.Frame(fenetre)
cadreResultat = tk.Frame(fenetre)
cadreArgent = tk.Frame(fenetre)

# - Options cadreChoix
cadreChoix['background'] = "#c900cc"
cadreChoix.grid(row=0, column=0,columnspan=3, sticky="nsew")

# - Options cadreResultat
cadreResultat['background'] = "#ffffff"
cadreResultat.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="nsew")

# - Options cadreArgent
cadreArgent['background'] = "#0000FF"
cadreArgent.grid(row=0, column=4, rowspan=4, sticky="nsew")

# - Titre pour cadreChoix
lblChoix = tk.Label(cadreChoix)
lblChoix['text'] = "Choix"
lblChoix['font'] = ["Arial", 30, "bold"]
lblChoix['bg'] = "#c900cc"
lblChoix.grid(row=0,column=0,columnspan=2, padx=100)

# - Titre pour cadreResultat
lblResultat = tk.Label(cadreResultat)
lblResultat['text'] = "Résultat"
lblResultat['font'] = ["Arial", 30, "bold"]
lblResultat['bg'] = "#ffffff"
lblResultat.grid(row=0,column=0,columnspan=2, padx=100)

# - Titre pour cadreArgent
lblArgent = tk.Label(cadreArgent)
lblArgent['text'] = "Argent"
lblArgent['font'] = ["Arial", 30, "bold"]
lblArgent['bg'] = "#0000FF"
lblArgent.grid(row=0,column=0,columnspan=2, padx=100)




fenetre.mainloop()