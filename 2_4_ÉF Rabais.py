# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 2.4.ÉF - Rabais
# Description : Calculer le prix des barbotines avec les rabais selon la quantité acheté
# ---------------------------------------------------------------------------------------------------------------------

# - Programme principal ------------------------------------------------------------------------------------------

# - Importation de modules ------------------------------------------------------------------------------------------
import math

# - Demander la quantité de barbotines voulu -----------------------------------------------------------------------------------------------
print("Ce programme calcule le prix des barbotines avec les rabais selon la quantité acheté")
print("Une barbotine coûte 4.99$\nSi vous achetez 10 ou plus vous recevez un rabais de 25%\nSi vous achetez entre 5 et 9 vous recevez un rabais de 15%")
qb = int(input("Combien de barbotines voulez-vous: "))

# - Calculer le prix et le rabais et afficher le résultat ----------------------------------------------------------------------------------------
prix = qb*4.99
if qb >= 10:
    rabais = prix*0.25
    pourcentage = "25%"
    total = prix-rabais
    print("Rabais: {:.2f}$\nVous sauvez: {}\nTotal: {:.2f}$".format(rabais, pourcentage, total))
else:
    if qb > 5 and qb < 9:
        rabais = prix*0.15
        pourcentage = "15%"
        total = prix-rabais
        print("Rabais: {:.2f}$\nVous sauvez: {}\nTotal: {:.2f}$".format(rabais, pourcentage, total))
    else:
        total = prix
        print("Total: {:.2f}$".format(total))

