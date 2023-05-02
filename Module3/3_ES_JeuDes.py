# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.ES.JeuDes
# Description : Interface graphique pour le jeu de dés crée dans 
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk
import random

# - Programme principal ------------------------------------------------------------------------------------------

# - Variables globales
global argent
argent_defaut = 100
argent = None
rondes = 0
personne = []


# - Argent de départ
# - Si le joueur a gagné ou perdu l'argent prendre la valeur de l'argent restant
if argent == None:
    argent = argent_defaut


# - Déclaration des fonctions

# - Jouer

def jouer():
    global argent, personne, mpari
    # - Verifier si l'argent parié est un nombre

    if pari.get().isdigit():
        print("Nombre")
        lblArgentError['text'] = ""
        if int(pari.get()) > argent:
            print("Pas assez d'argent")
            # - MAYBE ADD A THING TO CHECK IF THE NUMBER IS NEGATIVE
            lblArgentError['text'] = "Vous n'avez pas assez d'argent. \n Vous avez {}$" .format(argent)
        else:
            # - Assigner la valeur du pari à la variable mpari
            mpari = int(pari.get())
            # - Enlever le texte de lblArgentError
            lblArgentError['text'] = ""
            # - Si Alex est prédit
            if prediction.get() == "1":
                personne.append(1)
            # - Si Charles est prédit
            elif prediction.get() == "2":
                personne.append(2)
            # - Si Nul est prédit
            elif prediction.get() == "3":
                personne.append(3)
            else :
                lblArgentError['text'] = "Veuillez choisir une prédiction"
            # - Lancer les dés
            lancer()
    else:
        print("Pas un nombre")
        lblArgentError['text'] = "Veuillez entrer un nombre"

    print("Lancer")
    print(pari.get())

# - Lancer les dés
def lancer():
    # - Vairables globales
    global argent, personne, rf, mpari
    # - Lancer les dés de Alex
    d_o_1 = random.randint(1, 6)
    d_o_2 = random.randint(1, 6)
    d_o_3 = random.randint(1, 6)
    lblAlex1['text'] = d_o_1
    lblAlex2['text'] = d_o_2
    lblAlex3['text'] = d_o_3

    # - Lancer les dés de Charles
    d_j_1 = random.randint(1, 6)
    d_j_2 = random.randint(1, 6)
    d_j_3 = random.randint(1, 6)
    lblCharles1['text'] = d_j_1
    lblCharles2['text'] = d_j_2
    lblCharles3['text'] = d_j_3

    # - Calculer la somme des dés d'Alex et de Charles
    somme_o = d_o_1 + d_o_2 + d_o_3
    somme_j = d_j_1 + d_j_2 + d_j_3

    # - Prendre en compte les exceptions pour Alex
    if d_o_1 == d_o_2 == d_o_3:
        r_o = 8 + somme_o
    elif d_o_1 != d_o_2 != d_o_3:
        r_o = 5 + somme_o
    else:
        r_o = somme_o

    # - Prendre en compte les exceptions pour Charles
    if d_j_1 == d_j_2 == d_j_3:
        r_j = 8 + somme_j
    elif d_j_1 != d_j_2 != d_j_3:
        r_j = 5 + somme_j
    else:
        r_j = somme_j

    lblAlex['text'] = "Dés d'Alex: {}".format(r_o)
    lblCharles['text'] = "Dés de Charles: {}".format(r_j)

    # - Déterminer qui a gagné
    if r_o > r_j:
        r = "Alex a gagné!"
        lblGagnant['text'] = "Alex a gagné!"
    elif r_j > r_o:
        r = "Charles a gagné!"
        lblGagnant['text'] = "Charles a gagné!"
    else:
        r = "Match nul!"
        lblGagnant['text'] = "Match nul!"

   # - Si Alex a gagné
    if r == "Alex a gagné!":
        if personne == 1:
            argent += mpari
            lblArgentRestant['text'] = ("\nVous avez gagné {}$!".format(mpari))
        elif personne == 2 or personne == 3:
            argent -= mpari
            lblArgentRestant['text'] = ("\nVous avez perdu {}$!".format(mpari))

    # - Si Charles a gagné
    elif r == "Charles a gagné!":
        if personne == 2:
            argent += mpari
            lblArgentRestant['text'] = ("\nVous avez gagné {}$!".format(mpari))
        elif personne == 1 or personne == 3:
            argent -= mpari
            lblArgentRestant['text'] = ("\nVous avez perdu {}$!".format(mpari))

    # - Si le match est nul
    elif r == "Match nul!":
        if personne == 3:
            argent += mpari
            lblArgentRestant['text'] = ("\nVous avez gagné {}$!".format(mpari))
        elif personne == 1 or personne == 2:
            argent -= mpari
            lblArgentRestant['text'] = ("\nVous avez perdu {}$!".format(mpari))

    # - Afficher Erreur
    else:
        print("Erreur")

    # # - Si le joueur a perdu tout son argent
    # if argent <= 0:
    #     print("\n{0:-^50}\n".format(" Résultats "))
    #     print("Dés d'Alex: {} - {} - {}\nScore final d'Alex: {}".format(d_o_1, d_o_2, d_o_3, r_o))
    #     print("\nDés de Charles: {} - {} - {}\nScore final de Charles: {}".format(d_j_1, d_j_2, d_j_3, r_j))
    #     print("\n" + r)
    #     print("{0:-^50}".format(" Argent "))
    #     print(rf)
    #     print("\nVous avez maintenant {}$.".format(argent))
    #     print("\nVous avez perdu tout votre argent!")
    #     print("\n{0:-^50}".format(" Fin du jeu "))

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
btnLancer['command'] = jouer
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

# - Resultats Alex
lblAlex1 = tk.Label(cadreResultat)
lblAlex1['text'] = "0"
lblAlex1['font'] = ["Calibri", 15, "bold"]
lblAlex1['bg'] = "#ffffff"
lblAlex1.grid(row=1,column=0)

lblAlex2 = tk.Label(cadreResultat)
lblAlex2['text'] = "0"
lblAlex2['font'] = ["Calibri", 15, "bold"]
lblAlex2['bg'] = "#ffffff"
lblAlex2.grid(row=1,column=1)

lblAlex3 = tk.Label(cadreResultat)
lblAlex3['text'] = "0"
lblAlex3['font'] = ["Calibri", 15, "bold"]
lblAlex3['bg'] = "#ffffff"
lblAlex3.grid(row=1,column=2)

# - Label Alex
lblAlex = tk.Label(cadreResultat)
lblAlex['text'] = "Dés d'Alex"
lblAlex['font'] = ["Calibri", 15, "bold"]
lblAlex['bg'] = "#ffffff"
lblAlex.grid(row=2,column=0, columnspan= 3)


# - Resultats Charles
lblCharles1 = tk.Label(cadreResultat)
lblCharles1['text'] = "0"
lblCharles1['font'] = ["Calibri", 15, "bold"]
lblCharles1['bg'] = "#ffffff"
lblCharles1.grid(row=1,column=3)

lblCharles2 = tk.Label(cadreResultat)
lblCharles2['text'] = "0"
lblCharles2['font'] = ["Calibri", 15, "bold"]
lblCharles2['bg'] = "#ffffff"
lblCharles2.grid(row=1,column=4)

lblCharles3 = tk.Label(cadreResultat)
lblCharles3['text'] = "0"
lblCharles3['font'] = ["Calibri", 15, "bold"]
lblCharles3['bg'] = "#ffffff"
lblCharles3.grid(row=1,column=5)

# - Dés Charles
lblCharles = tk.Label(cadreResultat)
lblCharles['text'] = "Dés de Charles"
lblCharles['font'] = ["Calibri", 15, "bold"]
lblCharles['bg'] = "#ffffff"
lblCharles.grid(row=2,column=3, columnspan= 3)

# - Qui a gagné
lblGagnant = tk.Label(cadreResultat)
lblGagnant['text'] = ""
lblGagnant['font'] = ["Calibri", 15, "bold"]
lblGagnant['bg'] = "#ffffff"
lblGagnant.grid(row=3,column=0, columnspan= 3)

# - Argent restant
lblArgentRestant = tk.Label(cadreResultat)
lblArgentRestant['text'] = ""
lblArgentRestant['font'] = ["Calibri", 15, "bold"]
lblArgentRestant['bg'] = "#ffffff"
lblArgentRestant.grid(row=4,column=0, columnspan= 3)

fenetre.mainloop()