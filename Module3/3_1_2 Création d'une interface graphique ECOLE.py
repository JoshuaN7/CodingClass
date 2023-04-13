# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.1.2 Création d'une interface graphique
# Description : Interface Graphique pratique autonome
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Mon école")
fenetre.geometry("400x300")
fenetre.configure(bg = "#ffffff")

# - Texte Ecole
lblEcole = tk.Label(fenetre)
lblEcole ['text'] = "Franco-Ouest"
lblEcole ['font'] = ["Arial", 30, "bold"]
lblEcole ['bg'] = "#ffffff"
lblEcole.pack()

# - Texte Equipe
lblEquipe = tk.Label(fenetre)
lblEquipe ['text'] = "Équipe sportive"
lblEquipe ['font'] = ["Arial", 20]
lblEquipe ['bg'] = "#ffffff"
lblEquipe.pack()

fenetre.mainloop()