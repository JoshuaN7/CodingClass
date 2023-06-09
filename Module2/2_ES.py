# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 2.ES - Jeux de dés
# Description : Un jeu de dés où Alex et Charles jouent contre eux même. Le joueur doit prédire le gagnant du jeu.
# ---------------------------------------------------------------------------------------------------------------------

# - Programme principal ------------------------------------------------------------------------------------------

# - Importation de modules
import random

# - Le Jeu

# - Définir les variables globales
a_init = 100
# - Si le jeu vient d'être commencé et le joueur n'as pas encore gagné ou perdu l'argent prendre la valeur 100 comme le montant de départ
a_d = None
# - Si le joueur a gagné ou perdu l'argent prendre la valeur de l'argent restant
if a_d == None:
    a_d = a_init

# - Règles du jeu
print("{0:-^50}".format(" Règles du jeu "))
print("\nLe but du jeu est de prédire le gagnant du jeu.")
print("Tu peut parier sur Alex, Charles ou un match nul. Tu commences avec {}$".format(a_init))
print("-Si un des joueurs obtiennent 3 dés identiques, ils gangnent 8 points de plus sur leur somme des dés.")
print("-Si un des joueurs obtiennent 3 dés différents, ils gangnent 5 points de plus sur leur somme des dés.")


# - Demander au joueur de prédire le résultat
def prédire():

    # - Définir les variables globales
    global a, p, a_init, a_d

    # - Demander au jouer de prédire le résultat
    print("\n{0:-^50}".format(" Prédiction "))
    print("\nPrédisez le gagnant du jeu.")
    print("1 - Alex")
    print("2 - Charles")
    print("3 - Match nul")

    # - Prendre en compte les exceptions si p n'est pas un nombre
    try:
        p = int(input("\nVotre choix: "))
    except ValueError:
        print("\nVous devez choisir un nombre entre 1 et 3!")
        prédire()

    # - Prendre en compte les exceptions
    if p in [1, 2, 3]:
        a = int(input("\nCombien d'argent voulez-vous parier? Vous avez {}$: ".format(a_d)))
        if a > a_d:
            print("\nVous ne pouvez pas parier plus d'argent que vous n'en avez! Vous avez {}$".format(a_d))
            prédire()
        elif a < 0:
            print("\nVous ne pouvez pas parier un montant négatif!")
            prédire()
        else:
            jeu()

    # - Si le joueur n'a pas entré un nombre entre 1 et 3
    elif not isinstance(p, int):
        print("\nVous devez choisir un nombre entre 1 et 3!")
        prédire()
    else:
        print("\nVous devez choisir un nombre entre 1 et 3!")
        prédire()

# - Demander si le joueur veut rejouer
def rejouer():

    # - Définir les variables globales
    global a_d, a_init

    # - Demander si le joueur veut rejouer
    re = input("\nPour rejouer, appuyez sur la touche 'Entrée', si vous voulez quitter, appuyez sur 'q'.")
    if re == "":
    
    # - Si le joueur a gagné ou perdu l'argent prendre la valeur de l'argent restant
        if a_d <= 0:
            a_d = a_init
            prédire()
            jeu()
        else:
            prédire()
            jeu()

    # - Si le joueur veut quitter
    elif re == "q":
        print("\nMerci d'avoir joué!")
        exit()
    
    # - Si le joueur n'a pas appuyé sur la touche 'Entrée' ou sur 'q'
    else:
        print("\nVous devez appuyer sur la touche 'Entrée' ou sur 'q'!")
        rejouer()

# - Le jeu de base
def jeu():

    # - Définir les variables globales
    global a, p, a_init, a_d, rf

    # - Lancer les dés de Alex
    d_o_1 = random.randint(1, 6)
    d_o_2 = random.randint(1, 6)
    d_o_3 = random.randint(1, 6)

    # - Lancer les dés de Charles
    d_j_1 = random.randint(1, 6)
    d_j_2 = random.randint(1, 6)
    d_j_3 = random.randint(1, 6)

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

    # - Déterminer qui a gagné
    if r_o > r_j:
        r = "Alex a gagné!"
    elif r_j > r_o:
        r = "Charles a gagné!"
    else:
        r = "Match nul!"

   # - Si Alex a gagné
    if r == "Alex a gagné!":
        if p == 1:
            a_d += a
            rf = ("\nVous avez gagné {}$!".format(a))
        elif p == 2 or p == 3:
            a_d -= a
            rf = ("\nVous avez perdu {}$!".format(a))

    # - Si Charles a gagné
    elif r == "Charles a gagné!":
        if p == 2:
            a_d += a
            rf = ("\nVous avez gagné {}$!".format(a))
        elif p == 1 or p == 3:
            a_d -= a
            rf = ("\nVous avez perdu {}$!".format(a))

    # - Si le match est nul
    elif r == "Match nul!":
        if p == 3:
            a_d += a
            rf = ("\nVous avez gagné {}$!".format(a))
        elif p == 1 or p == 2:
            a_d -= a
            rf = ("\nVous avez perdu {}$!".format(a))

    # - Si le joueur a perdu tout son argent
    if a_d <= 0:
        print("\n{0:-^50}\n".format(" Résultats "))
        print("Dés d'Alex: {} - {} - {}\nScore final d'Alex: {}".format(d_o_1, d_o_2, d_o_3, r_o))
        print("\nDés de Charles: {} - {} - {}\nScore final de Charles: {}".format(d_j_1, d_j_2, d_j_3, r_j))
        print("\n" + r)
        print("{0:-^50}".format(" Argent "))
        print(rf)
        print("\nVous avez maintenant {}$.".format(a_d))
        print("\nVous avez perdu tout votre argent!")
        print("\n{0:-^50}".format(" Fin du jeu "))

        # - Demander si le joueur veut rejouer
        rejouer()
        
    # - Présenter les résultats
    print("\n{0:-^50}\n".format(" Résultats "))
    print("Dés d'Alex: {} - {} - {}\nScore final d'Alex: {}".format(d_o_1, d_o_2, d_o_3, r_o))
    print("\nDés de Charles: {} - {} - {}\nScore final de Charles: {}".format(d_j_1, d_j_2, d_j_3, r_j))
    print("\n" + r)
    print("{0:-^50}".format(" Argent "))
    print(rf)
    print("\nVous avez maintenant {}$.".format(a_d))
    rejouer()


# - Appel de la fonction pour commencer le programme
prédire()
jeu()