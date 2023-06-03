# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 4.2.EF - Probabilité Dés
# Description : Programme qui calcule la probabilité d'obtenir un certian nombre dans un certian nombre de lancers
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import random

# - Programme principal ------------------------------------------------------------------------------------------

# - Fonctions

# - Lancer les dés
def lancer():
    global des
    lancer = input("Combien de fois voulez-vous lancer les dés?: ")
    des = [] 
    for i in range(int(lancer)):
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        des.append(de1 + de2)
    calculs()
        
# - Calculer les probabilités
def calculs():
    global des

    # - Loop
    for i in des:

        # - Déclaration des variables
        un = 0
        deux = 0
        trois = 0
        quatre = 0
        cinq = 0
        six = 0
        sept = 0
        huit = 0
        neuf = 0
        dix = 0
        onze = 0
        douze = 0

        # - Ajouter 1 à la variable de fois que le nombre est sorti
        if i == 1:
            un += 1
        elif i == 2:
            deux += 1
        elif i == 3:
            trois += 1
        elif i == 4:
            quatre += 1
        elif i == 5:
            cinq += 1
        elif i == 6:
            six += 1
        elif i == 7:
            sept += 1
        elif i == 8:
            huit += 1
        elif i == 9:
            neuf += 1
        elif i == 10:
            dix += 1
        elif i == 11:
            onze += 1
        elif i == 12:
            douze += 1
        # - Si il y a une erreur
        else:
            print("Erreur")

    # - Afficher les résultats
    print("\n")
    print("{0:^20}{1:^20}{2:^20}".format("Somme des dés", "Nombre de fois", "Probabilité (%)"))
    print("{:.^60}".format("."))
    for x in range(1, 13):
        print("{0:^20}{1:^20}{2:^20.0f}".format(x, des.count(x), des.count(x) * 100 / len(des)))


# - Appel de la fonction
lancer()