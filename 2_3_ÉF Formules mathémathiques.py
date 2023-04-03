# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 2.3.ÉF - Formules Mathématiques
# Description : Calculer le résultat de la formule de Pythagore
# ---------------------------------------------------------------------------------------------------------------------

# - Programme principal ------------------------------------------------------------------------------------------

# - Importation de modules ------------------------------------------------------------------------------------------
import math

# - Demander pour la longueur des côtées -----------------------------------------------------------------------------------------------
print("Ce programme prend la longueur de l'hypothénuse et un cathète d'un triangle et trouve la longueur de l'autre cathète à l'aide du théorème de Pythagore")
c = int(input("Longueur de l'hypothénuse: "))
b = int(input("Longueur d'un cathète: "))

# - Calcule la longueur de l'autre cathète ----------------------------------------------------------------------------------------
a = math.sqrt(math.pow(c,2)-math.pow(b,2))

# - Affiche le résultat ---------------------------------------------------------------------------------------------
print("\nLa longueur de l'autre côté du triangle est: {}".format(a))
