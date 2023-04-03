# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 2.ES - Jeux de dés
# Description : Un jeu de dés où tu joues contre un ordinateur dans le but d'obtenir la plus grosse somme de dés.
# ---------------------------------------------------------------------------------------------------------------------

# - Programme principal ------------------------------------------------------------------------------------------

# - Importation de modules ------------------------------------------------------------------------------------------
import random

# - Lancer les dés de l'ordinateur -----------------------------------------------------------------------------------------------
d_o_1 = random.randint(1, 6)
d_o_2 = random.randint(1, 6)
d_o_3 = random.randint(1, 6)

# - Lancer les dés du joueur -----------------------------------------------------------------------------------------------
d_j_1 = random.randint(1, 6)
d_j_2 = random.randint(1, 6)
d_j_3 = random.randint(1, 6)

# - Calculer la somme des dés de l'ordinateur et du joueur -----------------------------------------------------------------------------------------------
somme_o = d_o_1 + d_o_2 + d_o_3
somme_j = d_j_1 + d_j_2 + d_j_3

# - Prendre en compte les exceptions pour l'ordinateur ------------------------------------------------------------------------------
if d_o_1 == d_o_2 == d_o_3:
    r_o = 8 + somme_o
elif d_o_1 != d_o_2 != d_o_3:
    r_o = 5 + somme_o
else:
    r_o = somme_o

# - Prendre en compte les exceptions pour le joueur ------------------------------------------------------------------------------
if d_j_1 == d_j_2 == d_j_3:
    r_j = 8 + somme_j
elif d_j_1 != d_j_2 != d_j_3:
    r_j = 5 + somme_j
else:
    r_j = somme_j

# - Déterminer qui a gagné ------------------------------------------------------------------------------
if r_o > r_j:
    r = "L'ordinateur a gagné!"
elif r_j > r_o:
    r = "Vous avez gagné!"
else:
    r = "Match nul!"

# - Calculer le prix et le rabais et afficher le résultat ----------------------------------------------------------------------------------------
print("\nRésultats:\n")
print("Dés de l'ordinateur: {} - {} - {}\nScore final de l'ordinateur: {}".format(d_o_1, d_o_2, d_o_3, r_o))
print("\nDés du joueur: {} - {} - {}\nScore final du joueur: {}".format(d_j_1, d_j_2, d_j_3, r_j))
print("\n" + r)
