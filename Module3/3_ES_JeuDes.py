# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.ES.JeuDes
# Description : Interface graphique pour le jeu de dés crée dans 
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Variables globales
argent = 100
rondes = 0


# - Déclaration des fonctions
def lancer():
    # - Verifier si l'argent parié est un nombre
    global prediction
    if pari.get().isdigit():
        print("Nombre")
        lblArgentError['text'] = ""
        if int(pari.get()) > argent:
            print("Pas assez d'argent")
            lblArgentError['text'] = "Vous n'avez pas assez d'argent"
        else:
            print("Assez d'argent")
            lblArgentError['text'] = ""
            # - Lancer les dés
            # - Si Alex est prédit
            if prediction == "1":
                print("Prédiction Alex")
            # - Si Charles est prédit
            elif prediction == "2":
                print("Prédiction Charles")
            # - Si Nul est prédit
            elif prediction == "3":
                print("Prédiction Nul")
    else:
        print("Pas un nombre")
        lblArgentError['text'] = "Veuillez entrer un nombre"

    print("Lancer")
    print(pari.get())

# - Fenetre
fenetre = tk.Tk()
fenetre.title("Jeu de dés")
fenetre.geometry("1200x500")
fenetre['bg'] = "#ffffff"

# - Création des cadres
cadreChoix = tk.Frame(fenetre)
cadreResultat = tk.Frame(fenetre)
cadreArgent = tk.Frame(fenetre)

# - Options cadreChoix
cadreChoix['background'] = "#ffffff"
cadreChoix['relief'] = "ridge"
cadreChoix['borderwidth'] = 3
cadreChoix.grid(row=0, column=0,columnspan=5, rowspan=2, sticky="nsew")

# - Options cadreResultat
cadreResultat['background'] = "#ffffff"
cadreResultat['relief'] = "ridge"
cadreResultat['borderwidth'] = 3
cadreResultat.grid(row=1, column=0, rowspan=4, columnspan=5, sticky="nsew")

# - Options cadreArgent
cadreArgent['background'] = "#ffffff"
cadreArgent['relief'] = "ridge"
cadreArgent['borderwidth'] = 3
cadreArgent.grid(row=0, column=4,columnspan=2, rowspan=5, sticky="nsew")

# - Configuration des lignes et colonnes
fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)
fenetre.rowconfigure(0, weight=1)
fenetre.rowconfigure(1, weight=1)
fenetre.rowconfigure(2, weight=1)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)

# - Titre pour cadreChoix
lblChoix = tk.Label(cadreChoix)
lblChoix['text'] = "Prédisiez le gagnant du jeu"
lblChoix['font'] = ["Calibri", 20, "bold"]
lblChoix['bg'] = "#ffffff"
lblChoix.grid(row=0,column=0,columnspan=3, padx=250)

# - Variable pour prediction
global prediction

prediction = tk.StringVar()

# - Option Alex
radAlex = tk.Radiobutton(cadreChoix)
radAlex['text'] = "Alex"
radAlex['font'] = ["Calibri", 15, "bold"]
radAlex['bg'] = "#ffffff"
radAlex['value'] = "1"
radAlex['variable'] = prediction
radAlex.select()
radAlex.grid(row=1,column=0)

# - Option Charles
radCharles = tk.Radiobutton(cadreChoix)
radCharles['text'] = "Charles"
radCharles['font'] = ["Calibri", 15, "bold"]
radCharles['bg'] = "#ffffff"
radCharles['value'] = "2"
radCharles['variable'] = prediction
radCharles.grid(row=1,column=1)

# - Option Égalité
radEgalite = tk.Radiobutton(cadreChoix)
radEgalite['text'] = "Égalité"
radEgalite['font'] = ["Calibri", 15, "bold"]
radEgalite['bg'] = "#ffffff"
radEgalite['value'] = "3"
radEgalite['variable'] = prediction
radEgalite.grid(row=1,column=2)

# - Bouton pour lancer les dés
btnLancer = tk.Button(cadreChoix)
btnLancer['text'] = "Lancer"
btnLancer['font'] = ["Calibri", 15, "bold"]
btnLancer['bg'] = "#ffffff"
btnLancer['command'] = lancer
btnLancer.grid(row=2,column=0,columnspan=3, padx=20)

# - Titre pour cadreResultat
lblResultat = tk.Label(cadreResultat)
lblResultat['text'] = "Résultat"
lblResultat['font'] = ["Calibri", 30, "bold"]
lblResultat['bg'] = "#ffffff"
lblResultat.grid(row=0,column=0,columnspan=2, padx=100)

# - Titre pour cadreArgent
lblArgent = tk.Label(cadreArgent)
lblArgent['text'] = "Argent"
lblArgent['font'] = ["Calibri", 15, "bold"]
lblArgent['bg'] = "#ffffff"
lblArgent.grid(row=0,column=0,columnspan=2)

# - Argent
lblArgent = tk.Label(cadreArgent)
lblArgent['text'] = str(argent) + "$"
lblArgent['font'] = ["Calibri", 15, "bold"]
lblArgent['bg'] = "#ffffff"
lblArgent.grid(row=1,column=0,columnspan=2)

# - Argent parié
lblArgentParie = tk.Label(cadreArgent)
lblArgentParie['text'] = "Pari"
lblArgentParie['font'] = ["Calibri", 15, "bold"]
lblArgentParie['bg'] = "#ffffff"
lblArgentParie.grid(row=2,column=0,columnspan=2)

# - Argent input
pari = tk.StringVar()
entArgent = tk.Entry(cadreArgent)
entArgent['font'] = ["Calibri", 15, "bold"]
entArgent['bg'] = "#ffffff"
entArgent['textvariable'] = pari
entArgent.grid(row=3,column=0,columnspan=2, padx=20)

# - Argent Error
lblArgentError = tk.Label(cadreArgent)
lblArgentError['text'] = ""
lblArgentError['font'] = ["Calibri", 15, "bold"]
lblArgentError['bg'] = "#ffffff"
lblArgentError.grid(row=4,column=0,columnspan=2)

fenetre.mainloop()