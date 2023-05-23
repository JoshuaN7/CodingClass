# ---------------------------------------------------------------------------------------------------------------------
# Nom : Sophie Pellerin
# Titre : ____
# Description : ____
# ---------------------------------------------------------------------------------------------------------------------

# - Importation des modules ------------------------------------------------------------------------------------------
import tkinter as tk
import random
# - Variables globales -----------------------------------------------------------------------------------------------

# Variable de qui a gagné
gagnantOrdi = 0
gagnantJoueur = 0
gagnantEgalite = 0

# Variable qui qui a augmenté de niveau
niveauOrdi = 0
niveauJoueur = 0

# - Déclaration des fonctions ----------------------------------------------------------------------------------------
def cliqueQuitter ():
    fenetre.destroy()
def cliqueRegles ():
    # - Créer le cadre
    cadreRegles = tk.Frame(fenetre)
    cadreRegles['background'] = "#26468A"
    cadreRegles['relief'] = "groove"
    cadreRegles['borderwidth'] = 3
    cadreRegles['width'] = 1000
    cadreRegles['height'] = 700
    cadreRegles.grid(row=0, column=0, sticky="nsew", padx=150, pady=100)

    # afficher le titre "Règles du jeu"
    lblRegles = tk.Label(cadreRegles)
    lblRegles['text'] = "Règles du jeu"
    lblRegles['font'] = ("Georgia", 18)
    lblRegles['fg'] = "#ffffff"
    lblRegles['bg'] = "#26468A"
    lblRegles.grid(row=0, column=2, sticky="nsew")

    # afficher les règles
    lblReglesListe = tk.Label(cadreRegles)
    lblReglesListe['text'] = "Vous allez jouer contre l'ordinateur et rouler 3 dés chacun.\n"\
                      "\nLes points seront calculés selon le barême suivant: "\
                      "\n- 3 dés identiques vaut 18 points + la somme des dés"\
                      "\n- 3 dés différents vaut 5 points + la somme des dés"\
                       "\n- Sinon, le nombre de points est seulement la somme des dés"\
                       "\n\nSi vous gagnez la ronde, vous monterez d'un niveau. Bonne chance!"
    lblReglesListe['font'] = ("Georgia", 15)
    lblReglesListe['fg'] = "#ffffff"
    lblReglesListe['bg'] = "#26468A"
    lblReglesListe.grid(row=1, column=2, sticky="nsew")

    # - Boutton pour retourner au jeu
    btnRetour = tk.Button(cadreRegles)
    btnRetour['text'] = "Retour"
    btnRetour['font'] = ("Georgia", 15)
    btnRetour['fg'] = "#000000"
    btnRetour['bg'] = "#ffffff"
    btnRetour['command'] = cadreRegles.destroy
    btnRetour.grid(row=2, column=2, columnspan=2, pady=20)

def cliqueJouer():
    global somme_jou, somme_ordi, lvl_jou, lvl_ordi, niveauJoueur, niveauOrdi, gagnantEgalite, gagnantJoueur, gagnantOrdi

    # Les dés de l'ordinateur (de = dé et ordi = ordinateur)
    de_ordi1 = random.randint(1, 6)
    de_ordi2 = random.randint(1, 6)
    de_ordi3 = random.randint(1, 6)
    # Les dés du joueur (de = dé et jou = joueur)
    de_jou1 = random.randint(1, 6)
    de_jou2 = random.randint(1, 6)
    de_jou3 = random.randint(1, 6)

    # La somme de chaque lancement des dés de l'ordinateur
    somme_ordi = de_ordi1 + de_ordi2 + de_ordi3
    # La somme de chaque lancement des dés du joueur
    somme_jou = de_jou1 + de_jou2 + de_jou3

    # Calculer la somme des dés de l'ordinateur
    somme_ordi = de_ordi1 + de_ordi2 + de_ordi3
    somme_jou = de_jou1 + de_jou2 + de_jou3

    # Calculer les points de l'ordinateur en utilisant les restrictions
    if de_ordi1 == de_ordi2 and de_ordi2 == de_ordi3:
        somme_ordi = 18 + somme_ordi
    elif de_ordi1 != de_ordi2 and de_ordi2 != de_ordi3 and de_ordi1 != de_ordi3:
        somme_ordi = 5 + somme_ordi

    # Calculer les points du joueur en utilisant les restrictions
    if de_jou1 == de_jou2 and de_jou2 == de_jou3:
        somme_jou = 18 + somme_jou
    elif de_jou1 != de_jou2 and de_jou2 != de_jou3 and de_jou1 != de_jou3:
        somme_jou = 5 + somme_jou

    # Lancer les dés de l'ordinateur
    lblDes1Ordi['image'] = des[de_ordi1-1]
    lblDes2Ordi['image'] = des[de_ordi2 - 1]
    lblDes3Ordi['image'] = des[de_ordi3 - 1]

    # Lancer les dés du joueur
    lblDes1Jou['image'] = des[de_jou1-1]
    lblDes2Jou['image'] = des[de_jou2-1]
    lblDes3Jou['image'] = des[de_jou3 - 1]

    # Démontrer qui a gagné
    if somme_jou > somme_ordi:
        gagnantJoueur += somme_jou
        lblPointageJoueur['text'] = gagnantJoueur
    elif somme_jou < somme_ordi:
        gagnantOrdi += somme_ordi
        lblPointageOrdi['text'] = gagnantOrdi
    else: 
        pass

    # Changement de niveaux
    if somme_jou > somme_ordi:
        niveauJoueur +=1
        lblNiveauJoueur['text'] = niveauJoueur

    elif somme_ordi > somme_jou:
        niveauOrdi +=1
        lblNiveauOrdi['text'] = niveauOrdi
    else: pass

def cliqueRecommancer():
    return

# Programme principale ---------------------------------------------------------------------------------------------
# FENÊTRE
fenetre = tk.Tk()
fenetre.option_add('*tearOff', False)
fenetre.title("Jeu de dés")
fenetre.geometry("1000x700")
fenetre['bg'] = "#26468A"



# IMAGES DES DÉS
des = [tk.PhotoImage(file='de1.gif'),
       tk.PhotoImage(file='de2.gif'),
       tk.PhotoImage(file='de3.gif'),
       tk.PhotoImage(file='de4.gif'),
       tk.PhotoImage(file='de5.gif'),
       tk.PhotoImage(file='de6.gif')]

# MENU - AIDE ET FICHIER (règlements du jeu et quitter le jeu)
# création de la barre de menu
mnuBarreMenu = tk.Menu(fenetre)
fenetre['menu'] = mnuBarreMenu
# création de l'objet menu
mnuFichier = tk.Menu(mnuBarreMenu)
# ajout du menu fichier
mnuBarreMenu.add_cascade(menu=mnuFichier, label="Fichier")
# ajout du menu aide
mnuAide = tk.Menu(mnuBarreMenu)
mnuBarreMenu.add_cascade(menu=mnuAide, label="Aide")
# ajout de la commande quitter sous le menu fichier
mnuFichier.add_command(label="Quitter", command=cliqueQuitter)
# ajout de la commande d'afficher les règles sous le menu d'aide
mnuAide.add_command(label="Règlements", command=cliqueRegles)

# - LE JEU -------------------------------------------------------------------------------------------------------------

# les cadres pour chaque section de la fenêtre du jeu
cadreDe = tk.Frame(fenetre)
cadreDe.grid(column=0, row=0)

cadreJou = tk.Frame(fenetre)
cadreJou.grid(column=0, row=1)

cadreOrdi = tk.Frame(fenetre)
cadreOrdi.grid(column=0, row=2)

cadreBtn = tk.Frame(fenetre)
cadreBtn.grid(column=0, row=3, columnspan=2)

cadreRes = tk.Frame(fenetre)
cadreRes.grid(column=1, row=0)

cadrePoints = tk.Frame(fenetre)
cadrePoints.grid(column=1, row=1)

cadreNiv = tk.Frame(fenetre)
cadreNiv.grid(column=1, row=2)

fenetre.grid_columnconfigure(0, weight=5)
fenetre.grid_columnconfigure(1, weight=2)

# Étiquette pour chaque cadre
# label pour le cadre De
lblDes = tk.Label(cadreDe)
lblDes['text'] = "DÉS"
lblDes['bg'] = "#26468A"
lblDes['fg'] = "#ffffff"
lblDes['font'] = "Georgia 36 bold"
lblDes.grid(column=0, row=0, padx=150, pady=20)

# label pour le cadre Res
lblResultats = tk.Label(cadreRes)
lblResultats['text'] = "RÉSULTATS"
lblResultats['bg'] = "#26468A"
lblResultats['fg'] = "#ffffff"
lblResultats['font'] = "Georgia 36 bold"
lblResultats.grid(column=0, row=0)

# label pour le cadre Jou
lblDesJoueurs = tk.Label(cadreJou)
lblDesJoueurs['text'] = "Joueur"
lblDesJoueurs['bg'] = "#26468A"
lblDesJoueurs['fg'] = "#ffffff"
lblDesJoueurs['font'] = "Georgia 28"
lblDesJoueurs.grid(column=0, row=0)

# label pour le cadre Ordi
lblDesOrdi = tk.Label(cadreOrdi)
lblDesOrdi['text'] = "Ordinateur"
lblDesOrdi['bg'] = "#26468A"
lblDesOrdi['fg'] = "#ffffff"
lblDesOrdi.grid(column=0, row=0)

# Afficher les dés du joueur
lblDes1Jou = tk.Label(cadreJou)
lblDes1Jou['image'] = des[0]
lblDes1Jou.grid(column=1, row=0)

lblDes2Jou = tk.Label(cadreJou)
lblDes2Jou['image'] = des[1]
lblDes2Jou.grid(column=2,row=0)

lblDes3Jou = tk.Label(cadreJou)
lblDes3Jou['image'] = des[2]
lblDes3Jou.grid(column=3, row=0)

# Afficher les dés de l'ordi
lblDes1Ordi = tk.Label(cadreOrdi)
lblDes1Ordi['image'] = des[0]
lblDes1Ordi.grid(column=1, row=0)

lblDes2Ordi = tk.Label(cadreOrdi)
lblDes2Ordi['image'] = des[1]
lblDes2Ordi.grid(column=2,row=0)

lblDes3Ordi = tk.Label(cadreOrdi)
lblDes3Ordi['image'] = des[2]
lblDes3Ordi.grid(column=3, row=0)

# Étiquettes pour le cadre de pointage
lblPointageTitre = tk.Label(cadrePoints)
lblPointageTitre['text'] = 'Pointage'
lblPointageTitre.grid(column=0, row=0, columnspan=2)

lblPointageJoueurTitre = tk.Label(cadrePoints)
lblPointageJoueurTitre['text'] = 'Joueur:'
lblPointageJoueurTitre.grid(column=0, row=1)

lblPointageJoueur = tk.Label(cadrePoints)
lblPointageJoueur['text'] = '0'
lblPointageJoueur.grid(column=0, row=2)

lblPointageOrdiTitre = tk.Label(cadrePoints)
lblPointageOrdiTitre['text'] = 'Ordinateur:'
lblPointageOrdiTitre.grid(column=1, row=1)

lblPointageOrdi = tk.Label(cadrePoints)
lblPointageOrdi['text'] = '0'
lblPointageOrdi.grid(column=1, row=2)

# Étiquettes pour le cadre de Niveau
lblNiveauTitre = tk.Label(cadreNiv)
lblNiveauTitre['text'] = 'Niveau'
lblNiveauTitre.grid(column=0, row=0, columnspan=2)

lblNiveauJoueurTitre = tk.Label(cadreNiv)
lblNiveauJoueurTitre['text'] = 'Joueur:'
lblNiveauJoueurTitre.grid(column=0, row=1)

lblNiveauJoueur = tk.Label(cadreNiv)
lblNiveauJoueur['text'] = '0'
lblNiveauJoueur.grid(column=0, row=2)

lblNiveauOrdiTitre = tk.Label(cadreNiv)
lblNiveauOrdiTitre['text'] = 'Ordinateur:'
lblNiveauOrdiTitre.grid(column=1, row=1)

lblNiveauOrdi = tk.Label(cadreNiv)
lblNiveauOrdi['text'] = '0'
lblNiveauOrdi.grid(column=1, row=2)

# Bouton pour jouer
btnJouer = tk.Button(cadreBtn)
btnJouer['text'] = 'Jouer'
btnJouer['command'] = cliqueJouer
btnJouer.grid(column=0, row=0, columnspan=1)

# Bouton pour recommencer
btnRecommencer = tk.Button(cadreBtn)
btnRecommencer['text'] = 'Recommencer'
btnRecommencer['command'] = cliqueRecommancer
btnRecommencer.grid(column=1, row=0, columnspan=1)
fenetre.mainloop()