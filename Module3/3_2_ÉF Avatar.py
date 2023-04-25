# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.2.ÉF Avatar
# Description : Interface graphique permettant l'utilisateur de créer un avatar
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Avatar")
fenetre.geometry("600x300")
fenetre.configure(bg = "#ffffff")

# - Création du cadre avec les résultats

cadreResultats = tk.Frame(fenetre)
cadreResultats['bg'] = "#ffffff"
cadreResultats['relief'] = "groove"
cadreResultats['borderwidth'] = 2
cadreResultats.pack(side=tk.RIGHT, expand=True, fill=tk.Y, ipadx=20)

# - Création du cadre d'options

cadreOptions = tk.Frame(fenetre)
cadreOptions['bg'] = "#ffffff"
cadreOptions['relief'] = "groove"
cadreOptions['borderwidth'] = 2
cadreOptions.pack(side=tk.LEFT)

# - Titre pour options de cheveux

lblCheveux = tk.Label(cadreOptions)
lblCheveux['text'] = "Options de Cheveux"
lblCheveux['font'] = ["Arial", 15, "bold"]
lblCheveux['bg'] = "#ffffff"
lblCheveux.pack(pady=(20,0))

# - Choix de cheveux
cheveux = tk.StringVar()

# - Cheveux
radCheveux = tk.Radiobutton(cadreOptions)
radCheveux['text'] = "Cheveux"
radCheveux['font'] = ["Arial", 15]
radCheveux['bg'] = "#ffffff"
radCheveux['value'] = "cheveux"
radCheveux['variable'] = cheveux
radCheveux.select()
radCheveux.pack()

# - Cheveux longs
radChauve = tk.Radiobutton(cadreOptions)
radChauve['text'] = "Chauve"
radChauve['font'] = ["Arial", 15]
radChauve['bg'] = "#ffffff"
radChauve['value'] = "chauve"
radChauve['variable'] = cheveux
radChauve.pack(anchor=tk.CENTER)

# - Images
imageChauve = tk.PhotoImage(file = r"C:\Users\josh8\OneDrive\Documents\ICS3U_python\Module3\Module3\1.gif")

# - Resultat
lblResultat = tk.Label(cadreResultats)
lblResultat['image'] = imageChauve
lblResultat.pack(padx=10, pady=10)

fenetre.mainloop()
