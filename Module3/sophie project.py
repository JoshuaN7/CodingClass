# ---------------------------------------------------------------------------------------------------------------------
# Nom : Sophie Pellerin
# Titre : Evaluation Sommative Unité 3 avec Tkinter
# Description : Jeu de dés contre l'ordinateur où le joueur et l'ordinateur lancent 3 dés chacun
#               et le joueur avec le plus de points gagne la ronde. Si le joueur gagne, il monte d'un niveau.
#               Les points sont calculés selon le barême trouvé dans les règlements. Les reglements sont accessibles
#               dans le menu sous la section d'aide. Le jeu est créé avec Tkinter et plusieurs cadres.
# ---------------------------------------------------------------------------------------------------------------------

# - Importation des modules ------------------------------------------------------------------------------------------
import tkinter as tk
import random

# - Variables globales -----------------------------------------------------------------------------------------------

# Variable de qui a gagné
gagnantOrdi = 0
gagnantJoueur = 0
gagnantEgalite = 0

# Variable qui a augmenté de niveau
niveauOrdi = 0
niveauJoueur = 0

# - Déclaration des fonctions ----------------------------------------------------------------------------------------
def cliqueQuitter():
    fenetre.destroy()

def cliqueRegles():
    # créer la fenetre
    fenetreRegles = tk.Tk()
    fenetreRegles.title("Règlements")
    fenetreRegles.geometry("650x400")
    fenetreRegles['bg'] = "#26468A"

    lblRegles = tk.Label(fenetreRegles)
    lblRegles['text'] = "Vous allez jouer contre l'ordinateur et rouler 3 dés chacun.\n" \
                             "\nLes points seront calculés selon le barême suivant: " \
                             "\n- 3 dés identiques vaut 18 points + la somme des dés" \
                             "\n- 3 dés différents vaut 5 points + la somme des dés" \
                             "\n- Sinon, le nombre de points est seulement la somme des dés" \
                             "\n\nSi vous gagnez la ronde, vous monterez d'un niveau. Bonne chance!"
    lblRegles['font'] = ("Georgia", 15)
    lblRegles['fg'] = "#ffffff"
    lblRegles['bg'] = "#26468A"
    lblRegles.grid(row=1, column=2, sticky="nsew", padx=20, pady=40)

    # - Boutton pour retourner au jeu
    btnRetour = tk.Button(fenetreRegles)
    btnRetour['text'] = "Retour"
    btnRetour['font'] = ("Georgia", 15)
    btnRetour['fg'] = "#000000"
    btnRetour['bg'] = "#ffffff"
    btnRetour['command'] = fenetreRegles.destroy
    btnRetour.grid(row=2, column=2, columnspan=2, pady=20)

def cliqueJouer():
    global somme_jou, somme_ordi, lvl_jou, lvl_ordi, niveauJoueur, niveauOrdi, gagnantEgalite, gagnantJoueur, gagnantOrdi, lblEgalite

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
    else: pass

    # Calculer les points du joueur en utilisant les restrictions
    if de_jou1 == de_jou2 and de_jou2 == de_jou3:
        somme_jou = 18 + somme_jou
    elif de_jou1 != de_jou2 and de_jou2 != de_jou3 and de_jou1 != de_jou3:
        somme_jou = 5 + somme_jou
    else: pass

    # Lancer les dés de l'ordinateur
    lblDes1Ordi['image'] = des[de_ordi1 - 1]
    lblDes2Ordi['image'] = des[de_ordi2 - 1]
    lblDes3Ordi['image'] = des[de_ordi3 - 1]

    # Lancer les dés du joueur
    lblDes1Jou['image'] = des[de_jou1 - 1]
    lblDes2Jou['image'] = des[de_jou2 - 1]
    lblDes3Jou['image'] = des[de_jou3 - 1]

    # Démontrer les dés lancés sous forme de numéro
    lblDes1JouNum['text'] = de_jou1
    lblDes2JouNum['text'] = de_jou2
    lblDes3JouNum['text'] = de_jou3
    lblDes1OrdiNum['text'] = de_ordi1
    lblDes2OrdiNum['text'] = de_ordi2
    lblDes3OrdiNum['text'] = de_ordi3

    # Démontrer qui a gagné
    if somme_jou > somme_ordi:
        gagnantJoueur += somme_jou
        lblPointageJoueur['text'] = gagnantJoueur
        lblEgalite['text'] = "Non"
    elif somme_jou < somme_ordi:
        gagnantOrdi += somme_ordi
        lblPointageOrdi['text'] = gagnantOrdi
        lblEgalite['text'] = "Non"
    elif somme_jou == somme_ordi:
        lblEgalite['text'] = "Oui"
    else: pass


    # Changement de niveaux
    if somme_jou > somme_ordi:
        niveauJoueur += 1
        lblNiveauJoueur['text'] = niveauJoueur

    elif somme_ordi > somme_jou:
        niveauOrdi += 1
        lblNiveauOrdi['text'] = niveauOrdi
    else:
        pass

def cliqueRecommencer():
    global somme_jou, somme_ordi, lvl_jou, lvl_ordi, niveauJoueur, niveauOrdi, gagnantEgalite, gagnantJoueur, gagnantOrdi, lblEgalite
    gagnantEgalite = 0
    gagnantOrdi = 0
    gagnantJoueur = 0
    niveauOrdi = 0
    niveauJoueur = 0
    lblNiveauOrdi['text'] = niveauOrdi
    lblNiveauJoueur['text'] = niveauJoueur
    lblPointageOrdi['text'] = gagnantOrdi
    lblPointageJoueur['text'] = gagnantJoueur
    lblEgalite['text'] = ""
    lblDes1Jou['image'] = des[0]
    lblDes2Jou['image'] = des[1]
    lblDes3Jou['image'] = des[2]
    lblDes1Ordi['image'] = des[0]
    lblDes2Ordi['image'] = des[1]
    lblDes3Ordi['image'] = des[2]
    lblDes1JouNum['text'] = ""
    lblDes2JouNum['text'] = ""
    lblDes3JouNum['text'] = ""
    lblDes1OrdiNum['text'] = ""
    lblDes2OrdiNum['text'] = ""
    lblDes3OrdiNum['text'] = ""

# - Programme principale ---------------------------------------------------------------------------------------------
# FENÊTRE DU JEU PRINCIPAL 
fenetre = tk.Tk()
fenetre.option_add('*tearOff', False)
fenetre.title("Jeu de dés")
fenetre.geometry("950x520")
fenetre['bg'] = "#26468A"

# IMAGES DES DÉS
des = [tk.PhotoImage(file='de1.gif'),
       tk.PhotoImage(file='de2.gif'),
       tk.PhotoImage(file='de3.gif'),
       tk.PhotoImage(file='de4.gif'),
       tk.PhotoImage(file='de5.gif'),
       tk.PhotoImage(file='de6.gif')]

# MENU - AIDE ET FICHIER (règlements du jeu et quitter le jeu)
# Création de la barre de menu
mnuBarreMenu = tk.Menu(fenetre)
fenetre['menu'] = mnuBarreMenu

# Création de l'objet menu
mnuFichier = tk.Menu(mnuBarreMenu)

# Ajout du menu fichier
mnuBarreMenu.add_cascade(menu=mnuFichier, label="Fichier")

# Ajout du menu aide
mnuAide = tk.Menu(mnuBarreMenu)
mnuBarreMenu.add_cascade(menu=mnuAide, label="Aide")

# Ajout de la commande quitter sous le menu fichier
mnuFichier.add_command(label="Quitter", command=cliqueQuitter)

# Ajout de la commande d'afficher les règles sous le menu d'aide
mnuAide.add_command(label="Règlements", command=cliqueRegles)

# L'ORGANISATION DU JEU 
# Les cadres pour chaque section de la fenêtre du jeu

# Cadre pour le titre "Dés"
cadreDe = tk.Frame(fenetre)
cadreDe['bg'] = "#26468A"
cadreDe.grid(column=0, row=0)

# Cadre pour les dés du joueur
cadreJou = tk.Frame(fenetre)
cadreJou['bg'] = "#26468A"
cadreJou.grid(column=0, row=1, pady=10)

# Cadre pour les dés de l'ordinateur
cadreOrdi = tk.Frame(fenetre)
cadreOrdi['bg'] = "#26468A"
cadreOrdi.grid(column=0, row=2, pady=10)

# Cadre pour le boutton "Jouer"
cadreBtnJouer = tk.Frame(fenetre)
cadreBtnJouer['bg'] = "#26468A"
cadreBtnJouer.grid(column=0, row=4, columnspan=1)

# Cadre pour le boutton "Recommencer"
cadreBtnRecommencer = tk.Frame(fenetre)
cadreBtnRecommencer['bg'] = "#26468A"
cadreBtnRecommencer.grid(column=1, row=4, columnspan=2)

# Cadre pour le titre "Résultats"
cadreRes = tk.Frame(fenetre)
cadreRes['bg']= "#26468A"
cadreRes.grid(column=1, row=0)

# Cadre pour le pointage
cadrePoints = tk.Frame(fenetre)
cadrePoints['bg'] = "#26468A"
cadrePoints.grid(column=1, row=1)

# Cadre pour les niveaux
cadreNiv = tk.Frame(fenetre)
cadreNiv['bg'] = "#26468A"
cadreNiv.grid(column=1, row=2)

# Cadre pour l'égalité
cadreEgalite = tk.Frame(fenetre)
cadreEgalite['bg'] = "#26468A"
cadreEgalite.grid(column=1, row=3)

fenetre.grid_columnconfigure(0, weight=5)
fenetre.grid_columnconfigure(1, weight=2)

# Étiquettes pour chaque cadre
# Label pour le cadre De
lblDes = tk.Label(cadreDe)
lblDes['text'] = "DÉS"
lblDes['bg'] = "#26468A"
lblDes['fg'] = "#ffffff"
lblDes['font'] = "Georgia 36 bold"
lblDes.grid(column=0, row=0, padx=150, pady=20)

# Label pour le cadre Res
lblResultats = tk.Label(cadreRes)
lblResultats['text'] = "RÉSULTATS"
lblResultats['bg'] = "#26468A"
lblResultats['fg'] = "#ffffff"
lblResultats['font'] = "Georgia 36 bold"
lblResultats.grid(column=0, row=0)

# Label pour le cadre Jou
lblDesJoueurs = tk.Label(cadreJou)
lblDesJoueurs['text'] = "Joueur"
lblDesJoueurs['bg'] = "#26468A"
lblDesJoueurs['fg'] = "#ffffff"
lblDesJoueurs['font'] = "Georgia 28"
lblDesJoueurs.grid(column=0, row=0, padx=34)

# Label pour le cadre Ordi
lblDesOrdi = tk.Label(cadreOrdi)
lblDesOrdi['text'] = "Ordinateur"
lblDesOrdi['bg'] = "#26468A"
lblDesOrdi['fg'] = "#ffffff"
lblDesOrdi['font'] = "Georgia 28"
lblDesOrdi.grid(column=0, row=0)

# Afficher le 1er dé du joueur
lblDes1Jou = tk.Label(cadreJou)
lblDes1Jou['image'] = des[0]
lblDes1Jou.grid(column=1, row=0, padx=10)

# Afficher le 2eme dé du joueur
lblDes2Jou = tk.Label(cadreJou)
lblDes2Jou['image'] = des[1]
lblDes2Jou.grid(column=2, row=0, padx=10)

# Afficher le 3eme dé du joueur
lblDes3Jou = tk.Label(cadreJou)
lblDes3Jou['image'] = des[2]
lblDes3Jou.grid(column=3, row=0, padx=10)

# Afficher le 1er dé de l'ordinateur
lblDes1Ordi = tk.Label(cadreOrdi)
lblDes1Ordi['image'] = des[0]
lblDes1Ordi.grid(column=1, row=0, padx=10)

# Afficher le 2eme dé de l'ordinateur
lblDes2Ordi = tk.Label(cadreOrdi)
lblDes2Ordi['image'] = des[1]
lblDes2Ordi.grid(column=2, row=0, padx=10)

# Afficher le 3eme dé de l'ordinateur
lblDes3Ordi = tk.Label(cadreOrdi)
lblDes3Ordi['image'] = des[2]
lblDes3Ordi.grid(column=3, row=0, padx=10)

# Étiquettes pour le cadre de pointage
# Étiquette pour le titre "Pointage"
lblPointageTitre = tk.Label(cadrePoints)
lblPointageTitre['text'] = 'Pointage'
lblPointageTitre['bg'] = "#26468A"
lblPointageTitre['fg'] = "#ffffff"
lblPointageTitre['font'] = "georgia 18"
lblPointageTitre.grid(column=0, row=0, columnspan=2)

# Étiquette pour le titre du pointage du joueur
lblPointageJoueurTitre = tk.Label(cadrePoints)
lblPointageJoueurTitre['text'] = 'Joueur:'
lblPointageJoueurTitre['bg'] = "#26468A"
lblPointageJoueurTitre['fg'] = "#ffffff"
lblPointageJoueurTitre['font'] = "georgia 14"
lblPointageJoueurTitre.grid(column=0, row=1, padx=15)

# Étiquette pour le pointage réel (les numéros) du joueur
lblPointageJoueur = tk.Label(cadrePoints)
lblPointageJoueur['text'] = '0'
lblPointageJoueur['bg'] = "#26468A"
lblPointageJoueur['fg'] = "#ffffff"
lblPointageJoueur['font'] = "georgia 14"
lblPointageJoueur.grid(column=0, row=2)

# Étiquette pour le titre du pointage de l'ordinateur
lblPointageOrdiTitre = tk.Label(cadrePoints)
lblPointageOrdiTitre['text'] = 'Ordinateur:'
lblPointageOrdiTitre['bg'] = "#26468A"
lblPointageOrdiTitre['fg'] = "#ffffff"
lblPointageOrdiTitre['font'] = "georgia 14"
lblPointageOrdiTitre.grid(column=1, row=1, padx=15)

# Étiquette pour le pointage réel (les numéros) de l'ordinateur
lblPointageOrdi = tk.Label(cadrePoints)
lblPointageOrdi['text'] = '0'
lblPointageOrdi['bg'] = "#26468A"
lblPointageOrdi['fg'] = "#ffffff"
lblPointageOrdi['font'] = "georgia 14"
lblPointageOrdi.grid(column=1, row=2)

# Étiquettes pour le cadre de Niveau
# Étiqueete pour le titre "Niveau"
lblNiveauTitre = tk.Label(cadreNiv)
lblNiveauTitre['text'] = 'Niveau'
lblNiveauTitre['bg'] = "#26468A"
lblNiveauTitre['fg'] = "#ffffff"
lblNiveauTitre['font'] = "georgia 18"
lblNiveauTitre.grid(column=0, row=0, columnspan=2)

# Étiquette pour le titre du niveau du joueur
lblNiveauJoueurTitre = tk.Label(cadreNiv)
lblNiveauJoueurTitre['text'] = 'Joueur:'
lblNiveauJoueurTitre['bg'] = "#26468A"
lblNiveauJoueurTitre['fg'] = "#ffffff"
lblNiveauJoueurTitre['font'] = "georgia 14"
lblNiveauJoueurTitre.grid(column=0, row=1, padx=15)

# Étiquette pour le niveau réel (les numéros) du joueur
lblNiveauJoueur = tk.Label(cadreNiv)
lblNiveauJoueur['text'] = '0'
lblNiveauJoueur['bg'] = "#26468A"
lblNiveauJoueur['fg'] = "#ffffff"
lblNiveauJoueur['font'] = "georgia 14"
lblNiveauJoueur.grid(column=0, row=2)

# Étiquette pour le titre du niveau de l'ordinateur
lblNiveauOrdiTitre = tk.Label(cadreNiv)
lblNiveauOrdiTitre['text'] = 'Ordinateur:'
lblNiveauOrdiTitre['bg'] = "#26468A"
lblNiveauOrdiTitre['fg'] = "#ffffff"
lblNiveauOrdiTitre['font'] = "georgia 14"
lblNiveauOrdiTitre.grid(column=1, row=1, padx=15)

# Étiquette pour le niveau réel (les numéros) de l'ordinateur
lblNiveauOrdi = tk.Label(cadreNiv)
lblNiveauOrdi['text'] = '0'
lblNiveauOrdi['bg'] = "#26468A"
lblNiveauOrdi['fg'] = "#ffffff"
lblNiveauOrdi['font'] = "georgia 14"
lblNiveauOrdi.grid(column=1, row=2)

# Étiquette pour l'égalité du jeu
lblEgaliteTitre = tk.Label(cadreEgalite)
lblEgaliteTitre['text'] = "Égalité!"
lblEgaliteTitre['bg'] = "#26468A"
lblEgaliteTitre['fg'] = "#ffffff"
lblEgaliteTitre['font'] = "Georgia 18"
lblEgaliteTitre.grid(column=0, row=0)

# Étiquette pour les résultats du jeu (si c'est réelement une égalité ou non)
lblEgalite = tk.Label(cadreEgalite)
lblEgalite['text'] = ""
lblEgalite['bg'] = "#26468A"
lblEgalite['fg'] = "#ffffff"
lblEgalite['font'] = "Georgia 14"
lblEgalite.grid(column=0, row=1)

# Démontrer les dés lancés sous forme de numéro
# Le 1er dé du joueur
lblDes1JouNum = tk.Label(cadreJou)
lblDes1JouNum['text'] = ""
lblDes1JouNum['bg'] = "#26468A"
lblDes1JouNum['fg'] = "#ffffff"
lblDes1JouNum['font'] = "Georgia 12"
lblDes1JouNum.grid(column=1, row=1)

# Le 2eme dé du joueur
lblDes2JouNum = tk.Label(cadreJou)
lblDes2JouNum['text'] = ""
lblDes2JouNum['bg'] = "#26468A"
lblDes2JouNum['fg'] = "#ffffff"
lblDes2JouNum['font'] = "Georgia 12"
lblDes2JouNum.grid(column=2, row=1)

# Le 3eme dé du joueur
lblDes3JouNum = tk.Label(cadreJou)
lblDes3JouNum['text'] = ""
lblDes3JouNum['bg'] = "#26468A"
lblDes3JouNum['fg'] = "#ffffff"
lblDes3JouNum['font'] = "Georgia 12"
lblDes3JouNum.grid(column=3, row = 1)

# Le 1er dé de l'ordinateur
lblDes1OrdiNum = tk.Label(cadreOrdi)
lblDes1OrdiNum['text'] = ""
lblDes1OrdiNum['bg'] = "#26468A"
lblDes1OrdiNum['fg'] = "#ffffff"
lblDes1OrdiNum['font'] = "Georgia 12"
lblDes1OrdiNum.grid(column=1, row=1)

# Le 2eme dé de l'ordinateur
lblDes2OrdiNum = tk.Label(cadreOrdi)
lblDes2OrdiNum['text'] = ""
lblDes2OrdiNum['bg'] = "#26468A"
lblDes2OrdiNum['fg'] = "#ffffff"
lblDes2OrdiNum['font'] = "Georgia 12"
lblDes2OrdiNum.grid(column=2, row=1)

# Le 3eme dé de l'ordinateur
lblDes3OrdiNum = tk.Label(cadreOrdi)
lblDes3OrdiNum['text'] =""
lblDes3OrdiNum['bg'] = "#26468A"
lblDes3OrdiNum['fg'] = "#ffffff"
lblDes3OrdiNum['font'] = "Georgia 12"
lblDes3OrdiNum.grid(column=3, row=1)

# Bouton pour jouer
btnJouer = tk.Button(cadreBtnJouer)
btnJouer['text'] = 'Jouer'
btnJouer['font'] = "Georgia 18"
btnJouer['command'] = cliqueJouer
btnJouer.grid(column=0, row=0, columnspan=1, pady=30)

# Bouton pour recommencer
btnRecommencer = tk.Button(cadreBtnRecommencer)
btnRecommencer['text'] = 'Recommencer'
btnRecommencer['font'] = "Georgia 18"
btnRecommencer['command'] = cliqueRecommencer
btnRecommencer.grid(column=1, row=0, pady=30)

fenetre.mainloop()