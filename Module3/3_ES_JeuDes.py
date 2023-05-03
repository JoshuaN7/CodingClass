# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.ES.JeuDes
# Description : Interface graphique pour le jeu de dés crée dans tkinter
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk
import random

# - Programme principal ------------------------------------------------------------------------------------------

# - Variables globales
argent_defaut = 100
argent = None
rondes = 0
alex = 0
charles = 0
nul = 0
personne = []


# - Argent de départ
# - Si le joueur a gagné ou perdu l'argent prendre la valeur de l'argent restant
if argent == None:
    argent = argent_defaut


# - Déclaration des fonctions

# - Jouer

def jouer():
    global argent, personne, mpari, rondes, alex, charles, nul

    # - Verifier si l'argent parié est un nombre
    if pari.get().isdigit():
        lblArgentError['text'] = ""
        if int(pari.get()) > argent:
            # - MAYBE ADD A THING TO CHECK IF THE NUMBER IS NEGATIVE
            lblArgentError['text'] = "Vous n'avez pas assez d'argent. \n Vous avez {}$" .format(argent)
        else:
            # - Assigner la valeur du pari à la variable mpari
            mpari = int(pari.get())
            # - Enlever le texte de lblArgentError
            lblArgentError['text'] = ""
            # - Si Alex est prédit
            if prediction.get() == "1":
                personne = 1
            # - Si Charles est prédit
            elif prediction.get() == "2":
                personne = 2
            # - Si Nul est prédit
            elif prediction.get() == "3":
                personne = 3
            else :
                lblArgentError['text'] = "Veuillez choisir une prédiction"

            # - Lancer les dés
            lancer()
    else:
        lblArgentError['text'] = "Veuillez entrer un nombre"

# - Lancer les dés
def lancer():
    # - Vairables globales
    global argent, personne, rf, mpari, rondes, alex, charles, nul

    # - Afficher le nombre de rondes
    rondes+=1
    lblRondes['text'] = "Rondes: {}".format(rondes)

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
        alex += 1
        lblVictoiresAlex['text'] = "Victoires Alex: {}".format(alex)
    elif r_j > r_o:
        r = "Charles a gagné!"
        charles += 1
        lblVictoiresCharles['text'] = "Victoires Charles: {}".format(charles)
    else:
        r = "Match nul!"
        nul += 1
        lblVictoiresNulles['text'] = "Match nul: {}".format(nul)
    
    # - Afficher le gagnant
    lblGagnant['text'] = r

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

    # - Si le joueur a perdu tout son argent
    if argent <= 0:
        # - Afficher que le joueur a perdu tout son argent
        lblArgentRestant['fg'] = "#ff0000"
        lblArgentRestant['text'] = ("\nVous avez perdu tout votre argent!\nClicquez sur rejouer pour recommencer!")
        # - Activer le bouton pour recommencer
        btnRejouer['state'] = "normal"

    # - Changer le texte pour lblArgent 
    lblArgent['text'] = str(argent) + "$"
# - Rejouer
def rejouer():
    # - Variables globales
    global argent, personne, rf, mpari, rondes, alex, charles, nul
    # - Réinitialiser les variables
    argent = 100
    rondes = 0
    alex = 0
    charles = 0
    nul = 0
    # - Effacer les entrées
    entArgent.delete(0, tk.END)

    # - Changer l'état du bouton rejouer
    btnRejouer['state'] = "disabled"

    # - Réinitialiser les labels
    lblArgent['text'] = str(argent) + "$"
    lblArgentRestant['text'] = ""
    lblAlex1['text'] = "0"
    lblAlex2['text'] = "0"
    lblAlex3['text'] = "0"
    lblCharles1['text'] = "0"
    lblCharles2['text'] = "0"
    lblCharles3['text'] = "0"
    lblAlex['text'] = "Dés d'Alex: 0"
    lblCharles['text'] = "Dés de Charles: 0"
    lblGagnant['text'] = ""
    lblGagnant['fg'] = "#000000"
    lblRondes['text'] = "Rondes: {}".format(rondes)
    lblVictoiresAlex['text'] = "Victoires Alex: {}".format(alex)
    lblVictoiresCharles['text'] = "Victoires Charles: {}".format(charles)
    lblVictoiresNulles['text'] = "Match nul: {}".format(nul)

def regles():
    # - Créer le cadre
    cadreRegles = tk.Frame(fenetre)
    cadreRegles['background'] = "#ffffff"
    cadreRegles['relief'] = "groove"
    cadreRegles['borderwidth'] = 3
    cadreRegles.grid(row=0, column=0, rowspan=5, columnspan=6, sticky="nsew")

    # - Afficher le titre
    lblRegles = tk.Label(cadreRegles)
    lblRegles['text'] = "Règles du jeu"
    lblRegles['font'] = ("Arial", 20)
    lblRegles['fg'] = "#000000"
    lblRegles['bg'] = "#ffffff"
    lblRegles.grid(row=0, column=2, columnspan=2, pady=50)

    # - Afficher les règles
    lblRegles1 = tk.Label(cadreRegles)
    lblRegles1['text'] = "-Le but du jeu est de prédire le gagnant du jeu.\n-Tu peut parier sur Alex, Charles ou un match nul.\n-Tu commences avec {}$\n-Si un des joueurs obtiennent 3 dés identiques, ils gangnent \n8 points de plus sur leur somme des dés.\n-Si un des joueurs obtiennent 3 dés différents, ils gangnent \n5 points de plus sur leur somme des dés.".format(argent_defaut)
    lblRegles1['font'] = ("Arial", 15)
    lblRegles1['fg'] = "#000000"
    lblRegles1['bg'] = "#ffffff"
    lblRegles1.grid(row=1, column=2, columnspan=2, padx=70, pady=20)

    # - Boutton pour retourner au jeu
    btnRetour = tk.Button(cadreRegles)
    btnRetour['text'] = "Retour"
    btnRetour['font'] = ("Arial", 15)
    btnRetour['fg'] = "#000000"
    btnRetour['bg'] = "#ffffff"
    btnRetour['command'] = cadreRegles.destroy
    btnRetour.grid(row=2, column=2, columnspan=2, pady=20)

def changerValeurs():

    # - Enregistrer les valeurs
    def enregistrer():
        # - Variables globales
        global argent_defaut, mpari_defaut, rondes_defaut, argent


        if entArgentDefaut.get().isdigit():

            # - Recommenncer le jeu
            rejouer()

            # - Enregistrer les valeurs
            argent_defaut = int(entArgentDefaut.get())
            argent = argent_defaut
        
            # - Détruire le cadre
            cadreValeurs.destroy()
            lblArgent['text'] = str(argent) + "$"
        else:
            # - Afficher un message d'erreur
            lblArgentDefautErreur['text'] = "Veuillez entrer un nombre!"

    cadreValeurs = tk.Frame(fenetre)
    cadreValeurs['background'] = "#ffffff"
    cadreValeurs['relief'] = "groove"
    cadreValeurs['borderwidth'] = 3
    cadreValeurs.grid(row=0, column=0, rowspan=5, columnspan=6, sticky="nsew")

    # - Afficher le titre
    lblValeurs = tk.Label(cadreValeurs)
    lblValeurs['text'] = "Changer les valeurs par défaut: "
    lblValeurs['font'] = ("Arial", 20)
    lblValeurs['bg'] = "#ffffff"
    lblValeurs['fg'] = "#000000"
    lblValeurs.grid(row=0, column=2, columnspan=2, padx=150)

    # - Argent Defaut
    lblArgentDefaut = tk.Label(cadreValeurs)
    lblArgentDefaut['text'] = "Argent par défaut:"
    lblArgentDefaut['font'] = ("Arial", 15)
    lblArgentDefaut['bg'] = "#ffffff"
    lblArgentDefaut['fg'] = "#000000"
    lblArgentDefaut.grid(row=1, column=2, pady=50)

    # - Entrée pour changer les valeurs
    entArgentDefaut = tk.Entry(cadreValeurs)
    entArgentDefaut['font'] = ("Arial", 15)
    entArgentDefaut['bg'] = "#ffffff"
    entArgentDefaut['fg'] = "#000000"
    entArgentDefaut.grid(row=1, column=3)

    # - Erreur
    lblArgentDefautErreur = tk.Label(cadreValeurs)
    lblArgentDefautErreur['text'] = ""
    lblArgentDefautErreur['font'] = ("Arial", 15)
    lblArgentDefautErreur['fg'] = "#ff0000"
    lblArgentDefautErreur['bg'] = "#ffffff"
    lblArgentDefautErreur.grid(row=2, column=2, columnspan=2)

    # - Boutton pour enregistrer les valeurs
    btnEnregistrer = tk.Button(cadreValeurs)
    btnEnregistrer['text'] = "Enregistrer"
    btnEnregistrer['font'] = ("Arial", 15)
    btnEnregistrer['bg'] = "#ffffff"
    btnEnregistrer['fg'] = "#000000"
    btnEnregistrer['command'] = enregistrer
    btnEnregistrer.grid(row=3, column=2, columnspan=2)

# - Fenetre
fenetre = tk.Tk()
fenetre.title("Jeu de dés")
fenetre.geometry("700x500")
fenetre['bg'] = "#ffffff"

# - Menu
mnuBarreMenu = tk.Menu(fenetre)
fenetre['menu'] = mnuBarreMenu

# - Création du menu pour règles
mnuRegles = tk.Menu(mnuBarreMenu, tearoff=0)
mnuBarreMenu.add_cascade(label="Aide", menu=mnuRegles)
mnuRegles.add_command(label="Règles", command=regles)

# - Création du menu pour changer les valeurs par défaut
mnuOptions = tk.Menu(mnuBarreMenu, tearoff=0)
mnuBarreMenu.add_cascade(label="Options", menu=mnuOptions)
mnuOptions.add_command(label="Changer les valeurs par défaut", command=changerValeurs)

# - Création du menu pour recommencer la joute
mnuOptions.add_command(label="Recommencer", command=rejouer)

# - Création des cadres
cadreChoix = tk.Frame(fenetre)
cadreResultat = tk.Frame(fenetre)
cadreArgent = tk.Frame(fenetre)
cadreScore = tk.Frame(fenetre)

# - Options cadreChoix
cadreChoix['background'] = "#ffffff"
cadreChoix['relief'] = "ridge"
cadreChoix['borderwidth'] = 3
cadreChoix.grid(row=0, column=0,columnspan=5, rowspan=3, sticky="nsew")

# - Options cadreResultat
cadreResultat['background'] = "#ffffff"
cadreResultat['relief'] = "ridge"
cadreResultat['borderwidth'] = 3
cadreResultat.grid(row=3, column=0, rowspan=3, columnspan=5, sticky="nsew")

# - Options cadreArgent
cadreArgent['background'] = "#ffffff"
cadreArgent['relief'] = "ridge"
cadreArgent['borderwidth'] = 3
cadreArgent.grid(row=0, column=5,columnspan=1, rowspan=5, sticky="nsew")

# - Options cadreScore
cadreScore['background'] = "#ffffff"
cadreScore['relief'] = "ridge"
cadreScore['borderwidth'] = 3
cadreScore.grid(row=3, column=5, columnspan=1, rowspan=2, sticky="nsew")

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
lblChoix['fg'] = "#000000"
lblChoix.grid(row=0,column=0, columnspan=3, padx=50)

prediction = tk.StringVar()

# - Option Alex
radAlex = tk.Radiobutton(cadreChoix)
radAlex['text'] = "Alex"
radAlex['font'] = ["Calibri", 15, "bold"]
radAlex['bg'] = "#ffffff"
radAlex['fg'] = "#000000"
radAlex['value'] = "1"
radAlex['variable'] = prediction
radAlex.select()
radAlex.grid(row=1,column=1)

# - Option Charles
radCharles = tk.Radiobutton(cadreChoix)
radCharles['text'] = "Charles"
radCharles['font'] = ["Calibri", 15, "bold"]
radCharles['bg'] = "#ffffff"
radCharles['fg'] = "#000000"
radCharles['value'] = "2"
radCharles['variable'] = prediction
radCharles.grid(row=2,column=1)

# - Option Égalité
radEgalite = tk.Radiobutton(cadreChoix)
radEgalite['text'] = "Égalité"
radEgalite['font'] = ["Calibri", 15, "bold"]
radEgalite['bg'] = "#ffffff"
radEgalite['fg'] = "#000000"
radEgalite['value'] = "3"
radEgalite['variable'] = prediction
radEgalite.grid(row=3,column=1)

# - Bouton pour lancer les dés
btnLancer = tk.Button(cadreChoix)
btnLancer['text'] = "Lancer"
btnLancer['font'] = ["Calibri", 15, "bold"]
btnLancer['bg'] = "#ffffff"
btnLancer['fg'] = "#000000"
btnLancer['command'] = jouer
btnLancer.grid(row=4,column=0, pady=10)

# - Bouton pour recommencer
btnRejouer = tk.Button(cadreChoix)
btnRejouer['text'] = "Rejouer"
btnRejouer['font'] = ["Calibri", 15, "bold"]
btnRejouer['bg'] = "#ffffff"
btnRejouer['fg'] = "#000000"
btnRejouer['command'] = rejouer
btnRejouer['state'] = 'disabled'
btnRejouer.grid(row=4,column=2)

# - Titre pour cadreResultat
lblResultat = tk.Label(cadreResultat)
lblResultat['text'] = "Résultat"
lblResultat['font'] = ["Calibri", 20, "bold"]
lblResultat['bg'] = "#ffffff"
lblResultat['fg'] = "#000000"
lblResultat.grid(row=0,column=0,columnspan=6, padx=160)

# - Titre pour cadreArgent
lblArgentt = tk.Label(cadreArgent)
lblArgentt['text'] = "Argent"
lblArgentt['font'] = ["Calibri", 20, "bold"]
lblArgentt['bg'] = "#ffffff"
lblArgentt['fg'] = "#000000"
lblArgentt.grid(row=0,column=0,columnspan=2, padx=95)

# - Argent
lblArgent = tk.Label(cadreArgent)
lblArgent['text'] = str(argent) + "$"
lblArgent['font'] = ["Calibri", 15, "bold"]
lblArgent['bg'] = "#ffffff"
lblArgent['fg'] = "#000000"
lblArgent.grid(row=1,column=0,columnspan=2)

# - Argent parié
lblArgentParie = tk.Label(cadreArgent)
lblArgentParie['text'] = "Pari"
lblArgentParie['font'] = ["Calibri", 15, "bold"]
lblArgentParie['bg'] = "#ffffff"
lblArgentParie['fg'] = "#000000"
lblArgentParie.grid(row=2,column=0,columnspan=2)

# - Argent input
pari = tk.StringVar()
entArgent = tk.Entry(cadreArgent)
entArgent['font'] = ["Calibri", 15, "bold"]
entArgent['bg'] = "#ffffff"
entArgent['fg'] = "#000000"
entArgent['textvariable'] = pari
entArgent.grid(row=3,column=0,columnspan=2, padx=20)

# - Argent Error
lblArgentError = tk.Label(cadreArgent)
lblArgentError['text'] = ""
lblArgentError['font'] = ["Calibri", 10, "bold"]
lblArgentError['fg'] = "#ff0000" 
lblArgentError['bg'] = "#ffffff"
lblArgentError.grid(row=4,column=0,columnspan=2)

# - Resultats Alex
lblAlex1 = tk.Label(cadreResultat)
lblAlex1['text'] = "0"
lblAlex1['font'] = ["Calibri", 15, "bold"]
lblAlex1['bg'] = "#ffffff"
lblAlex1['fg'] = "#000000"
lblAlex1.grid(row=1,column=0)

lblAlex2 = tk.Label(cadreResultat)
lblAlex2['text'] = "0"
lblAlex2['font'] = ["Calibri", 15, "bold"]
lblAlex2['bg'] = "#ffffff"
lblAlex2['fg'] = "#000000"
lblAlex2.grid(row=1,column=1)

lblAlex3 = tk.Label(cadreResultat)
lblAlex3['text'] = "0"
lblAlex3['font'] = ["Calibri", 15, "bold"]
lblAlex3['bg'] = "#ffffff"
lblAlex3['fg'] = "#000000"
lblAlex3.grid(row=1,column=2)

# - Label Alex
lblAlex = tk.Label(cadreResultat)
lblAlex['text'] = "Dés d'Alex: 0"
lblAlex['font'] = ["Calibri", 15, "bold"]
lblAlex['bg'] = "#ffffff"
lblAlex['fg'] = "#000000"
lblAlex.grid(row=2,column=0, columnspan= 3)


# - Resultats Charles
lblCharles1 = tk.Label(cadreResultat)
lblCharles1['text'] = "0"
lblCharles1['font'] = ["Calibri", 15, "bold"]
lblCharles1['bg'] = "#ffffff"
lblCharles1['fg'] = "#000000"
lblCharles1.grid(row=1,column=3)

lblCharles2 = tk.Label(cadreResultat)
lblCharles2['text'] = "0"
lblCharles2['font'] = ["Calibri", 15, "bold"]
lblCharles2['bg'] = "#ffffff"
lblCharles2['fg'] = "#000000"
lblCharles2.grid(row=1,column=4)

lblCharles3 = tk.Label(cadreResultat)
lblCharles3['text'] = "0"
lblCharles3['font'] = ["Calibri", 15, "bold"]
lblCharles3['bg'] = "#ffffff"
lblCharles3['fg'] = "#000000"
lblCharles3.grid(row=1,column=5)

# - Dés Charles
lblCharles = tk.Label(cadreResultat)
lblCharles['text'] = "Dés de Charles: 0"
lblCharles['font'] = ["Calibri", 15, "bold"]
lblCharles['bg'] = "#ffffff"
lblCharles['fg'] = "#000000"
lblCharles.grid(row=2,column=3, columnspan= 3)

# - Qui a gagné
lblGagnant = tk.Label(cadreResultat)
lblGagnant['text'] = ""
lblGagnant['font'] = ["Calibri", 15]
lblGagnant['bg'] = "#ffffff"
lblGagnant['fg'] = "#000000"
lblGagnant.grid(row=3,column=0, columnspan= 6)

# - Argent restant
lblArgentRestant = tk.Label(cadreResultat)
lblArgentRestant['text'] = ""
lblArgentRestant['font'] = ["Calibri", 15, "bold"]
lblArgentRestant['bg'] = "#ffffff"
lblArgentRestant['fg'] = "#000000"
lblArgentRestant.grid(row=4,column=0, columnspan= 6)

# - Titre pour cadreScore
lblScore = tk.Label(cadreScore)
lblScore['text'] = "Score"
lblScore['font'] = ["Calibri", 20, "bold"]
lblScore['bg'] = "#ffffff"
lblScore['fg'] = "#000000"
lblScore.grid(row=0,column=0, padx=100)

# - Rondes
lblRondes = tk.Label(cadreScore)
lblRondes['text'] = "Rondes: {}".format(rondes)
lblRondes['font'] = ["Calibri", 15]
lblRondes['bg'] = "#ffffff"
lblRondes['fg'] = "#000000"
lblRondes.grid(row=1,column=0)

# - Victoires Alex
lblVictoiresAlex = tk.Label(cadreScore)
lblVictoiresAlex['text'] = "Victoires Alex: {}".format(alex)
lblVictoiresAlex['font'] = ["Calibri", 15]
lblVictoiresAlex['bg'] = "#ffffff"
lblVictoiresAlex['fg'] = "#000000"
lblVictoiresAlex.grid(row=2,column=0)

# - Victoires Charles
lblVictoiresCharles = tk.Label(cadreScore)
lblVictoiresCharles['text'] = "Victoires Charles: {}".format(charles)
lblVictoiresCharles['font'] = ["Calibri", 15]
lblVictoiresCharles['bg'] = "#ffffff"
lblVictoiresCharles['fg'] = "#000000"
lblVictoiresCharles.grid(row=3,column=0)

# - Victoires nulles
lblVictoiresNulles = tk.Label(cadreScore)
lblVictoiresNulles['text'] = "Match nul: {}".format(nul)
lblVictoiresNulles['font'] = ["Calibri", 15]
lblVictoiresNulles['bg'] = "#ffffff"
lblVictoiresNulles['fg'] = "#000000"
lblVictoiresNulles.grid(row=4,column=0)


fenetre.mainloop()