# -------------------------------------------------------------------------
# Nom : Denis Berthelot
# Titre : Blackjack - Projet Exam
# Description : Un jeu de blackjack qui affiche des cartes et permet au joueur de miser de l'argent fictif
# -------------------------------------------------------------------------

# - Importation des modules -----------------------------------------------

import tkinter as tk
import random as r
import time as t

# - Variables globales ----------------------------------------------------

rondes = []
valeurdelutilisateur = []
valeurdelordinateur = []
cartesjoueur = []
cartesordinateur = []
mise = []
argent = [250]

# - Déclaration des fonctions ---------------------------------------------


# Définir la taille pour les menus
def cliqueNormal():
    fenetre.geometry("1104x621")


def cliqueXGrand():
    fenetre.geometry("1440x815")


def cliqueGrand():
    fenetre.geometry("1275x675")


def cliquePetit():
    fenetre.geometry("950x450")


# Permet de détruire la fenêtre avec un menu
def cliqueQuitter():
    fenetre.destroy()


# Crée la page du jeu
def start():
    # Crée la fondation pour le jeu, défini les parties nécessaires
    def reset():
        # Permet d'appeler une fonction pour distribuer les cartes
        def distribue():
            # Effectue les changements nécessaires aux boutons et aux labels
            btnCarte['state'] = tk.ACTIVE
            btnReste['state'] = tk.ACTIVE
            btnMiser['state'] = tk.DISABLED
            btnRejouer['state'] = tk.DISABLED
            btnMiser['text'] = "En jeu"
            lblInfo['text'] = "C'est à votre tour !"

            # Efface la valeur des cartes de chaque joueur
            valeurdelutilisateur.clear()
            valeurdelordinateur.clear()

            # Trouve la care de l'ordi et ajoute sa valeur au tableau
            valeurcarteordi1 = r.randint(2, 11)
            valeurdelordinateur.append(valeurcarteordi1)

            # Détermine quelle image afficher en fonction de la valeur pigée
            if valeurcarteordi1 < 10:
                lblCarteOrdi1['image'] = carteimage[valeurcarteordi1 - 1][r.randint(0, 3)]
            elif valeurcarteordi1 == 10:
                lblCarteOrdi1['image'] = carteimage[9][r.randint(0, 15)]
            else:
                lblCarteOrdi1['image'] = carteimage[0][r.randint(0, 3)]

            # Trouve la première carte de l'utilisateur et ajoute sa valeur au tableau
            valeurcarteutil1 = r.randint(2, 11)
            valeurdelutilisateur.append(valeurcarteutil1)

            # Détermine quelle image afficher en fonction de la valeur pigée
            if valeurcarteutil1 < 10:
                lblCarteUtil1['image'] = carteimage[valeurcarteutil1 - 1][r.randint(0, 3)]
            elif valeurcarteutil1 == 10:
                lblCarteUtil1['image'] = carteimage[9][r.randint(0, 15)]
            else:
                lblCarteUtil1['image'] = carteimage[0][r.randint(0, 3)]

            # Trouve la deuxième carte de l'utilisateur et ajoute sa valeur au tableau
            valeurcarteutil2 = r.randint(2, 11)
            valeurdelutilisateur.append(valeurcarteutil2)

            # Détermine quelle image afficher en fonction de la valeur pigée
            if valeurcarteutil2 < 10:
                lblCarteUtil2['image'] = carteimage[valeurcarteutil2 - 1][r.randint(0, 3)]
            elif valeurcarteutil2 == 10:
                lblCarteUtil2['image'] = carteimage[9][r.randint(0, 15)]
            else:
                lblCarteUtil2['image'] = carteimage[0][r.randint(0, 3)]

            # Détermine si changer un as (11) à un est nécessaire
            for i in range(len(valeurdelutilisateur)):
                if sum(valeurdelutilisateur) > 21 and (valeurdelutilisateur.count(11) > 0):
                    # Remplace l'as
                    valeurdelutilisateur.remove(11)
                    valeurdelutilisateur.append(1)
                else:
                    pass

            totalutil = sum(valeurdelutilisateur)

            # Trouve si un blackjack a été distribué pour le joueur
            if totalutil == 21:
                lblInfo['text'] = "       Blackjack !       "

                # Ajoute une plus grande quantité d'argent pour le blackjack
                argent.append(sum(argent) + 6 * (sum(mise)))
                argent.pop(0)
                mise.clear()

                # Change les commandes nécessaires pour rejouer
                btnRejouer['command'] = reset
                btnRejouer['state'] = tk.ACTIVE
                btnCarte['state'] = tk.DISABLED
                btnReste['state'] = tk.DISABLED

                fenetre.update_idletasks()
            else:
                # Montre le score de l'utilisateur
                lblSommeUtil['text'] = "Vous avez accumulé " + str(totalutil) + " points."

            fenetre.update_idletasks()

        def carteutil():
            # Trouve la valeur de la prochaine carte de l'utilisateur, et l'ajoute au tableau
            x = r.randint(2, 11)
            valeurdelutilisateur.append(x)

            # Détermine quelle image afficher
            if x < 10:
                imagecartepige = carteimage[x - 1][r.randint(0, 3)]
            elif x == 10:
                imagecartepige = carteimage[9][r.randint(0, 15)]
            else:
                imagecartepige = carteimage[0][r.randint(0, 3)]

            # Trouve si changer la valeur d'un as est nécessaire
            for i in range(len(valeurdelutilisateur)):
                if sum(valeurdelutilisateur) > 21 and (valeurdelutilisateur.count(11) > 0):
                    # Remplace l'as
                    valeurdelutilisateur.remove(11)
                    valeurdelutilisateur.append(1)
                else:
                    pass

            # Crée une place dans le cadre pour la nouvelle image
            cadreUtilisateur.grid_columnconfigure(len(cartesjoueur) + 3, weight=1)
            # Crée le nouveau label pour l'image
            cartesjoueur.append(tk.Label(cadreUtilisateur))
            # Détermine quelle image prendre
            cartesjoueur[len(cartesjoueur) - 1]['image'] = imagecartepige
            # Place la carte à l'endroit nécessaire
            cartesjoueur[len(cartesjoueur) - 1].grid(row=0, column=len(cartesjoueur) + 2)

            # Affiche la valeur accumulée par l'utilisateur
            valeurpresente = str(sum(valeurdelutilisateur))
            lblSommeUtil['text'] = "Vous avez accumulé " + valeurpresente + " points."
            lblSommeUtil.grid(row=1, column=0, columnspan=100)

            # Détermine si le joueur a dépassé 21
            if sum(valeurdelutilisateur) > 21:
                lblSommeUtil['text'] = "Vous avez accumulé " + valeurpresente + " points. C'est une défaite!"

                # Change les boutons et les labels correspondants
                btnCarte['state'] = tk.DISABLED
                btnReste['state'] = tk.DISABLED
                btnRejouer['state'] = tk.ACTIVE
                btnRejouer['command'] = reset
                lblInfo['text'] = "  L'ordi a gagné !  "

                # Ajoute une victoire aux rondes
                rondes.append(0)

                # Efface la mise
                mise.clear()

                fenetre.update_idletasks()

            fenetre.update()

        # Défini la fonction pour le reste (stand)
        def reste():
            # Change les boutons et les labels correspondants
            btnCarte['state'] = tk.DISABLED
            btnReste['state'] = tk.DISABLED

            lblInfo['text'] = "L'ordinateur pige ses cartes..."

            # Permet de choisir et afficher la deuxième carte de l'ordinateur
            valeurcarteordi2 = r.randint(2, 11)
            valeurdelordinateur.append(valeurcarteordi2)

            # Détermine quelle image utiliser
            if valeurcarteordi2 < 10:
                lblCarteOrdi2['image'] = carteimage[valeurcarteordi2 - 1][r.randint(0, 3)]
            elif valeurcarteordi2 == 10:
                lblCarteOrdi2['image'] = carteimage[9][r.randint(0, 15)]
            else:
                lblCarteOrdi2['image'] = carteimage[0][r.randint(0, 3)]

            # Affiche la valeur des cartes de l'ordinateur
            lblSommeOrdi['text'] = "L'ordinateur a accumulé " + str(sum(valeurdelordinateur)) + " points."

            # Détermine si un as doit changer à un
            for i in range(len(valeurdelordinateur)):
                if sum(valeurdelordinateur) > 21 and (valeurdelordinateur.count(11) > 0):
                    # Remplace l'as
                    valeurdelordinateur.remove(11)
                    valeurdelordinateur.append(1)
                else:
                    pass

            fenetre.update()

            # Attend un moment avant de piger la prochaine carte (plus réaliste)
            t.sleep(1)

            # Pige une carte si la valeur des cartes de l'ordinateur est sous 17
            while sum(valeurdelordinateur) < 17:
                # Si oui, une nouvelle carte est créée
                # Détermine la valeur de cette carte, et l'ajoute au tableau
                y = r.randint(2, 11)
                valeurdelordinateur.append(y)

                # Trouve quelle image associer
                if y < 10:
                    imagecartepigeordi = carteimage[y - 1][r.randint(0, 3)]
                elif y == 10:
                    imagecartepigeordi = carteimage[9][r.randint(0, 15)]
                else:
                    imagecartepigeordi = carteimage[0][r.randint(0, 3)]

                # Crée une place dans le cadre pour la nouvelle image
                cadreOrdinateur.grid_columnconfigure(len(cartesordinateur) + 3, weight=1)
                # Crée le nouveau label pour l'image
                cartesordinateur.append(tk.Label(cadreOrdinateur))
                # Détermine quelle image prendre
                cartesordinateur[len(cartesordinateur) - 1]['image'] = imagecartepigeordi
                # Place la carte à l'endroit nécessaire
                cartesordinateur[len(cartesordinateur) - 1].grid(row=0, column=len(cartesordinateur) + 2)

                # Détermine à nouveau si la valeur d'un as doit être changé à un
                for i in range(len(valeurdelordinateur)):
                    if sum(valeurdelordinateur) > 21 and (valeurdelordinateur.count(11) > 0):
                        # Remplace l'as
                        valeurdelordinateur.remove(11)
                        valeurdelordinateur.append(1)
                    else:
                        pass

                # Affiche la nouvelle valeur des cartes de l'ordinateur
                lblSommeOrdi['text'] = "L'ordinateur a accumulé " + str(sum(valeurdelordinateur)) + " points."

                fenetre.update()

                # Attend une période de temps avant de piger une autre carte (plus réaliste)
                t.sleep(1)

            # Permet de trouver le gagnant
            if sum(valeurdelordinateur) > 21:
                # Si l'ordinateur dépasse 21

                # Une victoire est ajoutée aux rondes
                rondes.append(1)

                # Les labels nécessaires affichent la victoire du joueur
                lblSommeOrdi['text'] = "L'ordinateur a accumulé " + str(sum(valeurdelordinateur)) \
                                       + " points. C'est une victoire pour vous !"
                lblInfo['text'] = "Vous avez gagné !"

                # L'argent de la mise est distribuée, puis effacée
                argent.append(sum(argent)+2*(sum(mise)))
                argent.pop(0)
                mise.clear()
            else:
                if sum(valeurdelutilisateur) > sum(valeurdelordinateur):
                    # Si le joueur a un plus grand total que l'ordinateur

                    # Une victoire est ajoutée aux rondes
                    rondes.append(1)

                    # Le label associé affiche la victoire
                    lblInfo['text'] = "Vous avez gagné !"

                    # L'argent de la mise est distribuée, puis effacée
                    argent.append(sum(argent) + 2 * (sum(mise)))
                    argent.pop(0)
                    mise.clear()

                elif sum(valeurdelutilisateur) < sum(valeurdelordinateur):
                    # Si le joueur a un plus petit total que l'ordi

                    # Une défaite est ajoutée aux rondes
                    rondes.append(0)

                    # Le label associé affiche la défaite
                    lblInfo['text'] = "  L'ordi a gagné !  "

                    # L'argent de la mise est effacée
                    mise.clear()

                else:
                    # Si les valeurs sont équivalentes (push)

                    # Une égalité est ajoutée aux rondes
                    rondes.append(2)

                    # Le label associé affiche l'égalité
                    lblInfo['text'] = "C'est une égalité !"

                    # Le joueur reçoit la valeur de sa mise (ne gagne rien, ne perd rien).
                    argent.append(sum(argent) + (sum(mise)))
                    argent.pop(0)

                    # L'argent de la mise est effacée
                    mise.clear()

            # Le bouton rejouer est réactivé
            btnRejouer['command'] = reset
            btnRejouer['state'] = tk.ACTIVE

            fenetre.update_idletasks()

        # Défini la fonction pour miser de l'argent
        def miser():
            if sum(argent) == 10:
                # Si la valeur de l'argent approche zéro, le joueur ne peut plus miser
                btnMiser['state'] = tk.DISABLED
            else:
                pass

            # Ajoute 10$ à la mise
            mise.append(10)

            # Enlève 10$ à l'argent
            argent.append(int(sum(argent) - 10))

            # Remplace le vieux montant d'argent avec le nouveau
            argent.pop(0)

            # Affiche le montant d'argent du joueur
            lblVotreArgent['text'] = "  Votre argent : " + str(sum(argent)) + "$  "

            # Associe les bonnes informations au bouton miser
            btnMiser['text'] = "Miser 10$"
            btnMiser['command'] = miser
            btnMiser['highlightbackground'] = "#000000"

            # Montre la valeur de l'argent misé
            lblMiseTotale['text'] = "   Argent misé : " + str(sum(mise)) + "$   "
            lblMiseTotale['font'] = "Times 15"

            fenetre.update()

        # FIN DE LA DÉFINITION DES FONCTIONS INTERNES

        # Crée le cadre pour l'ordinateur
        cadreOrdinateur = tk.Frame(fenetre)
        cadreOrdinateur['background'] = "#1e4620"
        cadreOrdinateur['relief'] = tk.GROOVE
        cadreOrdinateur['borderwidth'] = 3
        cadreOrdinateur.grid(row=0, column=0, sticky="nsew", rowspan=4, columnspan=2)

        # Organise le grid du cadre de l'ordinateur
        cadreOrdinateur.grid_rowconfigure(0, weight=4)
        cadreOrdinateur.grid_rowconfigure(1, weight=1)
        cadreOrdinateur.grid_columnconfigure(0, weight=1)
        cadreOrdinateur.grid_columnconfigure(1, weight=1)
        cadreOrdinateur.grid_propagate(False)

        # Crée le cadre pour l'utilisateur
        cadreUtilisateur = tk.Frame(fenetre)
        cadreUtilisateur['background'] = "#1e4620"
        cadreUtilisateur['relief'] = tk.GROOVE
        cadreUtilisateur['borderwidth'] = 3
        cadreUtilisateur.grid(row=5, column=0, sticky="nsew", rowspan=4, columnspan=2)

        # Organise le grid du cadre de l'utilisateur
        cadreUtilisateur.grid_rowconfigure(0, weight=4)
        cadreUtilisateur.grid_rowconfigure(1, weight=1)
        cadreUtilisateur.grid_columnconfigure(0, weight=1)
        cadreUtilisateur.grid_columnconfigure(1, weight=1)
        cadreUtilisateur.grid_propagate(False)

        # Dans cadre utilisateur ------------------------------------------------------------
        # Affiche le verso de la carte pour l'utilisateur
        lblCarteUtil1 = tk.Label(cadreUtilisateur)
        lblCarteUtil1['image'] = carteimageverso
        lblCarteUtil1.grid(row=0, column=0)

        # Affiche le verso de la deuxième carte pour l'utilisateur
        lblCarteUtil2 = tk.Label(cadreUtilisateur)
        lblCarteUtil2['image'] = carteimageverso
        lblCarteUtil2.grid(row=0, column=1)

        # Crée le label pour démontrer quelles cartes sont à l'utilisateur
        lblSommeUtil = tk.Label(cadreUtilisateur)
        lblSommeUtil['text'] = "Vos cartes"
        lblSommeUtil['font'] = "Times 20"
        lblSommeUtil['bg'] = "#1e4620"
        lblSommeUtil.grid(row=1, column=0, columnspan=2)

        # Dans cadre ordinateur ------------------------------------------------------------
        # Affiche le verso de la carte pour l'ordinateur
        lblCarteOrdi1 = tk.Label(cadreOrdinateur)
        lblCarteOrdi1['image'] = carteimageverso
        lblCarteOrdi1.grid(row=0, column=0)

        # Affiche la deuxième carte choisie pour l'ordinateur
        lblCarteOrdi2 = tk.Label(cadreOrdinateur)
        lblCarteOrdi2['image'] = carteimageverso
        lblCarteOrdi2.grid(row=0, column=1)

        # Crée le label pour démontrer quelles cartes sont à l'ordinateur
        lblSommeOrdi = tk.Label(cadreOrdinateur)
        lblSommeOrdi['text'] = "Les cartes de l'ordinateur"
        lblSommeOrdi['font'] = "Times 20"
        lblSommeOrdi['bg'] = "#1e4620"
        lblSommeOrdi.grid(row=1, column=0, columnspan=100)

        # Dans cadre choix ------------------------------------------------------------

        # Crée le label montrant où les options du joueur sont situés
        lblOptions = tk.Label(cadreChoix)
        lblOptions['text'] = "Vos options : "
        lblOptions['font'] = "Times 20"
        lblOptions['bg'] = "#000000"
        lblOptions.grid(row=0, column=0)

        # Crée le bouton pour piger une nouvelle carte
        btnCarte = tk.Button(cadreChoix)
        btnCarte['text'] = "Carte"
        btnCarte['command'] = carteutil
        btnCarte['highlightbackground'] = "#000000"
        btnCarte['state'] = tk.DISABLED
        btnCarte.grid(row=1, column=0)

        # Crée le bouton pour garder ses cartes
        btnReste = tk.Button(cadreChoix)
        btnReste['text'] = "Reste"
        btnReste['command'] = reste
        btnReste['highlightbackground'] = "#000000"
        btnReste['state'] = tk.DISABLED
        btnReste.grid(row=2, column=0)

        # Crée le bouton pour rejouer
        btnRejouer = tk.Button(cadreChoix)
        if len(rondes) > 0:
            # Affiche rejouer si l'utilisateur a plus qu'une ronde
            btnRejouer['text'] = "Rejouer"
        else:
            # Affiche jouer si l'utilisateur ne l'a pas encore fait
            btnRejouer['text'] = "Jouer"
        btnRejouer['command'] = distribue
        btnRejouer['highlightbackground'] = "#000000"
        btnRejouer['state'] = tk.ACTIVE
        btnRejouer.grid(row=3, column=0)

        # Dans cadre argent ------------------------------------------------------------

        # Crée le label pour démontrer la valeur de l'argent
        lblVotreArgent = tk.Label(cadreArgent)
        lblVotreArgent['text'] = " Votre argent : " + str(sum(argent)) + "$ "
        lblVotreArgent['font'] = "Times 20"
        lblVotreArgent['bg'] = "#000000"
        lblVotreArgent.grid(row=1, column=0)

        # Crée le bouton pour miser
        btnMiser = tk.Button(cadreArgent)
        btnMiser['text'] = "Miser 10$"
        btnMiser['command'] = miser
        btnMiser['highlightbackground'] = "#000000"
        btnMiser.grid(row=2, column=0)
        if sum(argent) == 0:
            # Si le joueur n'as plus d'argent, il peut déclarer banqueroute et recevoir 100$
            btnMiser['text'] = "Banqueroute (+100$)"
            argent.append(100)
            argent.pop(0)
        else:
            pass

        # Crée le label qui affichera la valeur misée
        lblMiseTotale = tk.Label(cadreArgent)
        lblMiseTotale['text'] = "Choisissez un montant"
        lblMiseTotale['font'] = "Times 15"
        lblMiseTotale['bg'] = "#000000"
        lblMiseTotale.grid(row=3, column=0)

        # Dans le cadre avec les informations ------------------------------------------------------------

        # Crée le label avec les informations pertinentes au jeu et les instructions
        lblInfo = tk.Label(cadreInformations)
        if len(rondes) > 0:
            lblInfo['text'] = "Misez, puis cliquez rejouer pour distribuer les cartes"
        else:
            lblInfo['text'] = "Misez, puis cliquez jouer pour commencer"
        lblInfo['font'] = "Times 35"
        lblInfo['bg'] = "#000000"
        lblInfo.grid(row=1, column=1)

        # Dans le cadre des statistiques ------------------------------------------------------------

        # Crée le label pour afficher où se trouvent les statistiques
        lblStatistiques = tk.Label(cadreStatistiques)
        lblStatistiques['text'] = "Statistiques : "
        lblStatistiques['font'] = "Times 20"
        lblStatistiques['bg'] = "#000000"
        lblStatistiques.grid(row=0, column=0)

        # Crée le label pour montrer les victoires
        lblVosVictoires = tk.Label(cadreStatistiques)
        lblVosVictoires['text'] = "Victoires : " + str(rondes.count(1))
        lblVosVictoires['font'] = "Times 15"
        lblVosVictoires['bg'] = "#000000"
        lblVosVictoires.grid(row=1, column=0)

        # Crée le label pour montrer les défaites
        lblVosDefaites = tk.Label(cadreStatistiques)
        lblVosDefaites['text'] = "Défaites : " + str(rondes.count(0))
        lblVosDefaites['font'] = "Times 15"
        lblVosDefaites['bg'] = "#000000"
        lblVosDefaites.grid(row=2, column=0)

        # Crée le label pour montrer les égalités
        lblMatchNul = tk.Label(cadreStatistiques)
        lblMatchNul['text'] = "Égalités (push) : " + str(rondes.count(2))
        lblMatchNul['font'] = "Times 15"
        lblMatchNul['bg'] = "#000000"
        lblMatchNul.grid(row=3, column=0)

        # Crée le label pour afficher le pourcentage du nombre de rondes gagnées
        lblPourcentage = tk.Label(cadreStatistiques)
        if len(rondes) > 0:
            # Affiche et fait le calcul
            lblPourcentage['text'] = " Matchs gagnés : {0:.0f}% ".format(
                ((int(rondes.count(1))) / (int(len(rondes))) * 100))
        else:
            # Si aucun match n'a été joué, n'affiche rien
            lblPourcentage['text'] = "N/A"
        lblPourcentage['font'] = "Times 15"
        lblPourcentage['bg'] = "#000000"
        lblPourcentage.grid(row=4, column=0)

        fenetre.update()

    # FIN DE LA DÉFINITION DES FONCTIONS INTERNES

    # Détruit le bouton et les labels créés auparavant.
    btnStart.destroy()
    lblRegles.destroy()
    lblIntro.destroy()

    # Définir les images dans un tableau ou comme variable
    carteimageverso = tk.PhotoImage(file='0.gif')

    carteimage = [[tk.PhotoImage(file='1.gif'), tk.PhotoImage(file='14.gif'),
                   tk.PhotoImage(file='27.gif'), tk.PhotoImage(file='40.gif')
                   ],
                  [tk.PhotoImage(file='2.gif'), tk.PhotoImage(file='15.gif'),
                   tk.PhotoImage(file='28.gif'), tk.PhotoImage(file='41.gif')
                   ],
                  [tk.PhotoImage(file='3.gif'), tk.PhotoImage(file='16.gif'),
                   tk.PhotoImage(file='29.gif'), tk.PhotoImage(file='42.gif')
                   ],
                  [tk.PhotoImage(file='4.gif'), tk.PhotoImage(file='17.gif'),
                   tk.PhotoImage(file='30.gif'), tk.PhotoImage(file='43.gif')
                   ],
                  [tk.PhotoImage(file='5.gif'), tk.PhotoImage(file='18.gif'),
                   tk.PhotoImage(file='31.gif'), tk.PhotoImage(file='44.gif')
                   ],
                  [tk.PhotoImage(file='6.gif'), tk.PhotoImage(file='19.gif'),
                   tk.PhotoImage(file='32.gif'), tk.PhotoImage(file='45.gif')
                   ],
                  [tk.PhotoImage(file='7.gif'), tk.PhotoImage(file='20.gif'),
                   tk.PhotoImage(file='33.gif'), tk.PhotoImage(file='46.gif')
                   ],
                  [tk.PhotoImage(file='8.gif'), tk.PhotoImage(file='21.gif'),
                   tk.PhotoImage(file='34.gif'), tk.PhotoImage(file='47.gif')
                   ],
                  [tk.PhotoImage(file='9.gif'), tk.PhotoImage(file='22.gif'),
                   tk.PhotoImage(file='35.gif'), tk.PhotoImage(file='48.gif')
                   ],
                  [tk.PhotoImage(file='10.gif'), tk.PhotoImage(file='23.gif'),
                   tk.PhotoImage(file='36.gif'), tk.PhotoImage(file='49.gif'),
                   tk.PhotoImage(file='11.gif'), tk.PhotoImage(file='12.gif'),
                   tk.PhotoImage(file='13.gif'), tk.PhotoImage(file='24.gif'),
                   tk.PhotoImage(file='25.gif'), tk.PhotoImage(file='26.gif'),
                   tk.PhotoImage(file='37.gif'), tk.PhotoImage(file='38.gif'),
                   tk.PhotoImage(file='39.gif'), tk.PhotoImage(file='50.gif'),
                   tk.PhotoImage(file='51.gif'), tk.PhotoImage(file='52.gif')
                   ]
                  ]

    # Crée le cadre avec les choix du jeu
    cadreChoix = tk.Frame(fenetre)
    cadreChoix['background'] = "#000000"
    cadreChoix['relief'] = tk.GROOVE
    cadreChoix['borderwidth'] = 3
    cadreChoix.grid(row=0, column=2, sticky="nsew", rowspan=3)
    cadreChoix.grid_propagate(False)

    # Crée le cadre avec l'argent
    cadreArgent = tk.Frame(fenetre)
    cadreArgent['background'] = "#000000"
    cadreArgent['relief'] = tk.GROOVE
    cadreArgent['borderwidth'] = 3
    cadreArgent.grid(row=3, column=2, sticky="nsew", rowspan=3)
    cadreArgent.grid_propagate(False)

    # Crée le cadre avec les statistiques
    cadreStatistiques = tk.Frame(fenetre)
    cadreStatistiques['background'] = "#000000"
    cadreStatistiques['relief'] = tk.GROOVE
    cadreStatistiques['borderwidth'] = 3
    cadreStatistiques.grid(row=6, column=2, sticky="nsew", rowspan=3)
    cadreStatistiques.grid_propagate(False)

    # Crée le cadre avec les informations
    cadreInformations = tk.Frame(fenetre)
    cadreInformations['background'] = "#000000"
    cadreInformations['borderwidth'] = 3
    cadreInformations['relief'] = tk.GROOVE
    cadreInformations.grid(row=4, column=0, sticky="nsew", columnspan=2)
    cadreInformations.grid_propagate(False)

    # Organise le grid du cadre choix
    cadreChoix.grid_rowconfigure(0, weight=2)
    cadreChoix.grid_rowconfigure(1, weight=1)
    cadreChoix.grid_rowconfigure(2, weight=1)
    cadreChoix.grid_rowconfigure(3, weight=1)
    cadreChoix.grid_columnconfigure(0, weight=1)

    # Organise le grid du cadre argent
    cadreArgent.grid_rowconfigure(0, weight=1)
    cadreArgent.grid_rowconfigure(1, weight=1)
    cadreArgent.grid_rowconfigure(2, weight=1)
    cadreArgent.grid_rowconfigure(3, weight=1)
    cadreArgent.grid_rowconfigure(4, weight=1)
    cadreArgent.grid_columnconfigure(0, weight=1)

    # Organise le grid du cadre des statistiques
    cadreStatistiques.grid_rowconfigure(0, weight=2)
    cadreStatistiques.grid_rowconfigure(1, weight=1)
    cadreStatistiques.grid_rowconfigure(2, weight=1)
    cadreStatistiques.grid_rowconfigure(3, weight=1)
    cadreStatistiques.grid_rowconfigure(4, weight=1)
    cadreStatistiques.grid_columnconfigure(0, weight=1)

    # Organise le grid du cadre avec les informations
    cadreInformations.grid_rowconfigure(0, weight=1)
    cadreInformations.grid_rowconfigure(1, weight=1)
    cadreInformations.grid_rowconfigure(2, weight=1)
    cadreInformations.grid_columnconfigure(0, weight=1)
    cadreInformations.grid_columnconfigure(1, weight=1)
    cadreInformations.grid_columnconfigure(2, weight=1)

    fenetre.update()

    # Appelle la fonction reset
    reset()


# Défini la page principale
def pageprincipale():
    # Affiche le label intro
    lblIntro['text'] = "BIENVENUE AU BLACKJACK"
    lblIntro['font'] = "Times 50"
    lblIntro['fg'] = "#ffffff"
    lblIntro['bg'] = "#1e4620"
    lblIntro.pack(pady=30)

    # Affiche le bouton pour commencer
    btnStart['text'] = "COMMENCER !"
    btnStart['command'] = start
    btnStart['height'] = 2
    btnStart['font'] = "Times 14"
    btnStart['activeforeground'] = "#ff0000"
    btnStart['highlightbackground'] = "#1e4620"
    btnStart.pack()

    # Change et affiche le texte du label règles
    lblRegles['text'] = "Le blackjack est un jeu dans lequel le joueur essaie d'accumuler des cartes " \
                        "qui font une somme de 21, sans dépasser ce nombre. " \
                        "\n \nPour piger une nouvelle carte, le bouton affichant 'Carte' peut être cliqué. " \
                        "Si vous souhaitez garder vos cartes, cliquez 'Reste'. " \
                        "\nCeci mettra fin à votre tour et permettra à l'ordinateur de jouer. " \
                        "\n\nLe joueur débute avec 250$, qui peut être misé par bonds de 10$. À noter qu'il " \
                        "n'est pas nécessaire de miser de l'argent." \
                        "\nLorsque le joueur gagne, il recevra le double de sa mise. Lors d'une défaite, " \
                        "le joueur perdra le montant misé. " \
                        "\nObtenir un Blackjack triple la valeur de la mise. \nSi vous perdez l'entièreté de votre " \
                        "argent, 100$ additionnels vous seront alloués." \
                        "\n\nLes boutons pertinents seront présents en haut à droite de votre écran." \
                        "\n\nDans cette version du jeu, le as vaut 11 par défaut, mais peut changer à " \
                        "1 si le joueur dépasse 21." \
                        "\n\nSi vous êtes prêt, cliquez 'COMMENCER' !" \
                        "\nBonne chance !"
    lblRegles['font'] = "Times 20"
    lblRegles['bg'] = "#1e4620"
    lblRegles.pack(pady=20)

# - Programme principal ---------------------------------------------------


# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre['bg'] = "#1e4620"
fenetre['relief'] = tk.GROOVE
fenetre['border'] = 3
fenetre.title("Blackjack")
fenetre.geometry("1104x621")

# Dans la fenêtre principale -----------------------------------------------------------------------------
btnStart = tk.Button(fenetre)
lblRegles = tk.Label(fenetre)
lblIntro = tk.Label(fenetre)

# Crée la barre de menu
mnuBarreMenu = tk.Menu(fenetre)
fenetre['menu'] = mnuBarreMenu
mnuFichier = tk.Menu(mnuBarreMenu)
mnuBarreMenu.add_cascade(menu=mnuFichier, label="Fichier")

# Ajoute les commandes dans la barre fichier
mnuFichier.add_command(label="Écran X-Grand", command=cliqueXGrand)
mnuFichier.add_command(label="Écran Grand", command=cliqueGrand)
mnuFichier.add_command(label="Écran Normal", command=cliqueNormal)
mnuFichier.add_command(label="Écran Petit (Non-Recommandé)", command=cliquePetit)
mnuFichier.add_separator()
mnuFichier.add_command(label="Quitter", command=cliqueQuitter)

# Configuration des rangées/colonnes
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)
fenetre.grid_rowconfigure(3, weight=1)
fenetre.grid_rowconfigure(4, weight=1)
fenetre.grid_rowconfigure(5, weight=1)
fenetre.grid_rowconfigure(6, weight=1)
fenetre.grid_rowconfigure(7, weight=1)
fenetre.grid_rowconfigure(8, weight=1)
fenetre.grid_columnconfigure(0, weight=2)
fenetre.grid_columnconfigure(1, weight=2)
fenetre.grid_columnconfigure(2, weight=1)

# Appelle la fonction pour créer la page principale
pageprincipale()

# Affiche le programme
fenetre.mainloop()
