# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 2.3.1 Simplification de fractions
# Description : Simplifier les fractions
# ---------------------------------------------------------------------------------------------------------------------

# - Programme principal ------------------------------------------------------------------------------------------
import math

# - Demander pour la fraction -----------------------------------------------------------------------------------------------
print("Ce programme prend une fraction et le simplifie")
num = int(input("Numérateur: "))
deno = int(input("Dénominateur: "))

# - Trouve le plus petit facteur commun ----------------------------------------------------------------------------------------
fact = math.gcd(num, deno)
numsimple = num // fact
denosimple = deno // fact

# - Affiche le résultat ---------------------------------------------------------------------------------------------
print("\nLa fraction simplifiée est {}/{} et la fraction non simplifiée est {}/{}".format(numsimple, denosimple, num, deno))