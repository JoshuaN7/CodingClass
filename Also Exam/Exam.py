'''
Projet final 3 - Comptabilité

Description :
Le programme comptable minimaliste ci-dessous doit être amélioré.
Le programme doit demander plus d'information que simplement le nombre d'heures travaillées.
Il faut s'assurer d'envoyer un message d'erreur si l'utilisateur n'entre pas la bonne information en répondant à la question.
L'utilisateur doit saisir le nombre d'heures de travail de 5 employés minimum et calculer le montant de leur chèque de paie.
Ajouter des postes dans l'entreprise avec des salaires horaires différents.
   Par exemple, dans un restaurant, il pourrait y avoir 1-hôtesse, 2-serveur/serveuse, 3-plongueur, 4-cuisinier.
À la fin, le programme doit afficher un bilan à l'utilisateur.
   Par exemple, Employé : Jean-Luc Marchand - Poste occupé : plongeur -  Chèque à émettre: 45,80$

Conseils:
Assurer une bonne communication avec l'utilisateur.
Faire des ajouts pour rendre l'expérience usager intéressante.
'''

# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Examen Final
# Description : Interface graphique pour un programme de comptabilité
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Variables
TEST = False

# - Pages
entreesParPage = 10
entreesParPageRecherche = 5
page_courant = 1
page_courant_recherche = 1

# - Employés, postes, groupes
employes = []
groupes = []
groupesrecherche = []
postesoptions = {
   'Cuisinier' : 19.00,
   'Serveur' : 15.50,
   'Plongeur' : 28.98,
   'Caissier' : 15.98
}

# - Chiffres importants qui affectent le salaire
impot_retenu = 0.105  #10,5% de retenu sur le salaire
heures_pour_bonis = 160
bonis = 5

# - Recherche
types = ["Nom", "Prenom", "Poste", "Heures", "Salaire"]
employesTrouves = []

# - Couleurs
arriereplan1 = '#8cbbf1'
arriereplan2 = '#d7dde9'
boites = '#fdfdff'

# - Fonctions
def calcul_salaire(heures, taux_horaire):

   global impot_retenu, heures_pour_bonis, bonis
   nb_heures = int(heures)
   heurespourbonis = int(heures_pour_bonis)
   salaire = nb_heures * taux_horaire
   if nb_heures >=heurespourbonis:
      salaire = salaire*(1+bonis/100)
   else:
      pass
   impot = salaire * impot_retenu
   salaire_net = salaire - impot
   return salaire_net
   
# - Ajouter des entrées
def ajouter():
   # - Variables globales
   global employes, postesoptions, TEST

   # - Supprimer le label d'erreur s'il existe
   try:
      lblErreur.destroy()
   except:
      pass
   # - Si tous les entrées sont remplis et ne sont pas des espaces ajouter l'entrée dans la liste
   if nom.get() and prenom.get() and heures.get() and nom.get().isspace() == False and prenom.get().isspace() == False and heures.get().isspace() == False:
      try:
         # - vérifier si le nombre d'heures est un nombre
         x = float(heures.get())
         # - vérifier si le poste est choisi
         if poste.get() == "Poste":
            erreur("Veuillez choisir un poste", "EmployersEntry")
         else:
            # - Ajouter à rows
            employe = {
               "nom": nom.get(),
               "prenom": prenom.get(),
               "poste": poste.get(),
               "heures": heures.get(),
               "salaire": calcul_salaire(heures.get(), postesoptions.get(poste.get()))
            }
            # - Ajouter à la liste des employés
            employes.append(employe)
            # - Séparer les employés en groupes selon le nombre d'entrées par page
            grouper("Ajout")
            # - Si TEST est True, ne pas effacer les entrées pour faciliter les entrées lors du testing
            if TEST == True:
               pass
            else:
            # - Si TEST est False, effacer les entrées
               clear()
      # - Afficher les erreurs
      except:
         erreur("Le nombre d'heures doit être un nombre", "EmployersEntry")
   else:
      erreur("Veuillez remplir tous les champs", "EmployersEntry")

# - Effacer les entrées
def clear():
   entNom.delete(0, tk.END)
   entPrenom.delete(0, tk.END)
   entHeures.delete(0, tk.END)

# - Séparer les employés en groupes selon le nombre d'entrées par page
def grouper(x):

   # - Variables globales
   global entreesParPage, employes, groupes, groupesrecherche, entreesParPageRecherche, employesTrouves

   if x == "Recherche":
      groupesrecherche.clear()
      nombreEmployes = len(employesTrouves)
      nombreGroupes = nombreEmployes // entreesParPageRecherche + (nombreEmployes % entreesParPageRecherche > 0)

      # - Séparer les employés en groupes selon le nombre d'entrées par page
      for i in range(nombreGroupes):
         debut = i * entreesParPageRecherche
         fin = (i+1) * entreesParPageRecherche
         groupe = employesTrouves[debut:fin]
         groupesrecherche.append(groupe)

      # - Mettre à jour le tableau de groupes
      update("recherche")
   else:
      # - Effacer la liste des groupes pour faire la mise a jour du tableau de groupes
      groupes.clear()
      nombreEmployes = len(employes)
      nombreGroupes = nombreEmployes // entreesParPage + (nombreEmployes % entreesParPage > 0)

      # - Séparer les employés en groupes selon le nombre d'entrées par page
      for i in range(nombreGroupes):
         debut = i * entreesParPage
         fin = (i+1) * entreesParPage
         groupe = employes[debut:fin]
         groupes.append(groupe)

      # - Mettre à jour le tableau de groupes
      update("Ajout")

# - Mettre à jour les pages
def updatePage(x):
   # - Variables globales
      global page_courant, groupes, groupesrecherche, page_courant_recherche

      # - Mettre à jour les pages por la fenêtre de recherche
      if x == "Recherche":
         lblPagee['text'] = "Page {} sur {}".format(page_courant_recherche, len(groupesrecherche))
      # - Mettre à jour les pages por la fenêtre d'ajout
      else:
         lblPage['text'] = "Page {} sur {}".format(page_courant, len(groupes))

# - Passer à la page suivante pour la fenêtre d'ajout
def prochain():
   global page_courant, groupes
   nombreGroupes = len(groupes)
   if page_courant < nombreGroupes:
      page_courant += 1
      update("Ajout")

# - Revenir à la page précédente pour la fenêtre d'ajout
def precedent():
   global page_courant, groupes
   if page_courant > 1:
      page_courant -= 1
      update("Ajout")

# - Passer à la page suivante pour la fenêtre de recherche
def prochainRecherche():
   global page_courant_recherche, groupesrecherche
   nombreGroupes = len(groupesrecherche)
   if page_courant_recherche < nombreGroupes:
      page_courant_recherche += 1
      update("recherche")

# - Revenir à la page précédente pour la fenêtre de recherche
def precedentRecherche():
   global page_courant_recherche, groupesrecherche
   if page_courant_recherche > 1:
      page_courant_recherche -= 1
      update("recherche")

# - Rechercher un employé qui correspond à la recherche
def search():
    
    # - Variables globales
    global typeRecherche, motcle, employesTrouves, lblErreur, rowsrecherche, page_courant_recherche

    # - Renitialiser la page courante de la fenêtre de recherche
    page_courant_recherche = 1
    # - Effacer les erreurs
    try: 
        lblErreur.destroy()
    except:
        pass
    # - Effacer les employés trouvés
    employesTrouves.clear()

    # - Verifier si les champs sont remplis
    if motcle.get() and typeRecherche.get():
      recherche = motcle.get()
      typeSearch = typeRecherche.get()

      # - Vérifier si la recherche doit être un nombre
      if typeSearch == "Salaire" or typeSearch == "Heures":
          
         # - Vérifier si la recherche est un nombre
          if sinombre(recherche) == True:
                
                # - Pour tous les employés, vérifier si la recherche correspond à un des employés
                for i in employes:
                   
                   # - Si la recherche correspond à un des employés, ajouter l'employé à la liste des employés trouvés
                   if float(recherche) == float(i[typeSearch.lower()]):
                     employesTrouves.append(i)
                     grouper("Recherche")
                   # - Sinon, passer à l'employé suivant
                   else:
                     pass
            # - Si la recherche n'est pas un nombre, afficher une erreur
          else:
            erreur("La recherche doit être un nombre", "Recherche")

          # - Si aucun employé n'a été trouvé, afficher une erreur
          if len(employesTrouves) == 0:
               erreur("Aucun résultat trouvé", "Recherche")
          else:
               
         # - Sinon, mettre à jour le tableau des résultats
               update("recherche")

      # - Si la recherche ne doit pas être un nombre
      elif typeSearch == "Nom" or typeSearch == "Prenom" or typeSearch == "Poste":
          
          # - Pour tous les employés, vérifier si la recherche correspond à un des employés
          for i in employes:
             
             # - Si la recherche correspond à un des employés, ajouter l'employé à la liste des employés trouvés
             if recherche.lower() in i[typeSearch.lower()].lower():
               employesTrouves.append(i)
               grouper("Recherche")
            # - Sinon, passer à l'employé suivant
             else:
               pass
               
         # - Si aucun employé n'a été trouvé, afficher une erreur
          if len(employesTrouves) == 0:
               erreur("Aucun résultat trouvé", "Recherche")
          else:
               
            # - Sinon, mettre à jour le tableau des résultats
               update("recherche")

      # - Si les champs ne sont pas remplis, afficher une erreur
      else:
         erreur("Veuillez remplir tous les champs", "Recherche")

# - Fenêtre de recherche
def popupRecherche():
   
   # - Variables globales
   global typeRecherche, motcle, recherche, lblErreur, cadreRecherche, cadreResultat, lblTxtNom, lblTxtPrenom, lblTxtPoste, lblTxtHeures, lblTxtSalaire, lblPagee

   # - Créer la fenêtre de recherche
   recherche = tk.Toplevel()
   recherche.title("Rechercher")
   recherche.geometry("830x480")
   recherche['bg'] = '#ffffff'

   # - Configurer la fenêtre de recherche
   recherche.rowconfigure(0, weight=1)
   recherche.rowconfigure(1, weight=1)
   recherche.rowconfigure(2, weight=1)
   recherche.rowconfigure(3, weight=1)
   recherche.columnconfigure(0, weight=1)
   recherche.columnconfigure(1, weight=1)
   recherche.columnconfigure(2, weight=1)
   recherche.columnconfigure(3, weight=1)

   # - Créer le cadre de recherche
   cadreRecherche = tk.Frame(recherche)
   cadreRecherche['bg'] = arriereplan1
   cadreRecherche.grid(row=0, column=0, columnspan=4, sticky='nsew')

   # - Configurer le cadre de recherche
   cadreRecherche.rowconfigure(0, weight=1)
   cadreRecherche.rowconfigure(1, weight=1)
   cadreRecherche.rowconfigure(2, weight=1)
   cadreRecherche.columnconfigure(0, weight=1)
   cadreRecherche.columnconfigure(1, weight=1)
   cadreRecherche.columnconfigure(2, weight=1)

   # - Créer le cadre de résultat
   cadreResultat = tk.Frame(recherche)
   cadreResultat['bg'] = '#ffffff'
   cadreResultat.grid(row=1, column=0, columnspan=4, rowspan=3, sticky='nsew')
   cadreResultat.grid_propagate(0)

   # - Rechercher
   lblRecherche = tk.Label(cadreRecherche)
   lblRecherche['text'] = "Rechercher"
   lblRecherche['bg'] = arriereplan1
   lblRecherche['fg'] = '#000000'
   lblRecherche['font'] = ('Calibri', '12', 'bold')
   lblRecherche.grid(row=0, column=0)

   # - Type de recherche
   lblType = tk.Label(cadreRecherche)
   lblType['text'] = "Type de recherche"
   lblType['bg'] = arriereplan1
   lblType['fg'] = '#000000'
   lblType['font'] = ('Calibri', '12', 'bold')
   lblType.grid(row=0, column=1)

   # - Erreur
   lblErreur = tk.Label(cadreRecherche)
   lblErreur['text'] = ""
   lblErreur['bg'] = arriereplan1
   lblErreur['fg'] = '#ff0000'
   lblErreur['font'] = ('Calibri', '12', 'bold')
   lblErreur.grid(row=0, column=3)

   # - Champ de recherche
   motcle = tk.StringVar()
   entRecherche = tk.Entry(cadreRecherche)
   entRecherche['bg'] = boites
   entRecherche['fg'] = '#000000'
   entRecherche['textvariable'] = motcle
   entRecherche['font'] = ('Calibri', '12')
   entRecherche.grid(row=1, column=0)

   # - Type de recherche
   typeRecherche = tk.StringVar()
   typeRecherche.set("Nom")
   dropType = tk.OptionMenu(cadreRecherche, typeRecherche, *types)
   dropType['bg'] = boites
   dropType['fg'] = '#000000'
   dropType['font'] = ('Calibri', '12')
   dropType.grid(row=1, column=1)

   # - Bouton rechercher
   btnRechercher = tk.Button(cadreRecherche)
   btnRechercher['text'] = "Rechercher"
   btnRechercher['bg'] = boites
   btnRechercher['fg'] = '#000000'
   btnRechercher['font'] = ('Calibri', '12', 'bold')
   btnRechercher['command'] = search
   btnRechercher.grid(row=1, column=2, pady=20)

   # - Titre du tableau
   lblTxtNom = tk.Label(cadreResultat)
   lblTxtNom['text'] = 'Nom'
   lblTxtNom['bg'] = arriereplan2
   lblTxtNom['fg'] = '#000000'
   lblTxtNom['width'] = 20
   lblTxtNom['height'] = 2
   lblTxtNom['borderwidth'] = 2
   lblTxtNom['relief'] = 'groove'
   lblTxtNom['font'] = ('Calibri', '12', 'bold')
   lblTxtNom.grid(row=0, column=0)

   # - Titre du tableau
   lblTxtPrenom = tk.Label(cadreResultat)
   lblTxtPrenom['text'] = 'Prénom'
   lblTxtPrenom['bg'] = arriereplan2
   lblTxtPrenom['fg'] = '#000000'
   lblTxtPrenom['width'] = 20
   lblTxtPrenom['height'] = 2
   lblTxtPrenom['borderwidth'] = 2
   lblTxtPrenom['relief'] = 'groove'
   lblTxtPrenom['font'] = ('Calibri', '12', 'bold')
   lblTxtPrenom.grid(row=0, column=1)

   # - Titre du tableau
   lblTxtPoste = tk.Label(cadreResultat)
   lblTxtPoste['text'] = 'Poste'
   lblTxtPoste['bg'] = arriereplan2
   lblTxtPoste['fg'] = '#000000'
   lblTxtPoste['width'] = 20
   lblTxtPoste['height'] = 2
   lblTxtPoste['borderwidth'] = 2
   lblTxtPoste['relief'] = 'groove'
   lblTxtPoste['font'] = ('Calibri', '12', 'bold')
   lblTxtPoste.grid(row=0, column=2)

   # - Titre du tableau
   lblTxtHeures = tk.Label(cadreResultat)
   lblTxtHeures['text'] = 'Heures'
   lblTxtHeures['bg'] = arriereplan2
   lblTxtHeures['fg'] = '#000000'
   lblTxtHeures['width'] = 20
   lblTxtHeures['height'] = 2
   lblTxtHeures['borderwidth'] = 2
   lblTxtHeures['relief'] = 'groove'
   lblTxtHeures['font'] = ('Calibri', '12', 'bold')
   lblTxtHeures.grid(row=0, column=3)

   # - Titre du tableau
   lblTxtSalaire = tk.Label(cadreResultat)
   lblTxtSalaire['text'] = 'Salaire'
   lblTxtSalaire['bg'] = arriereplan2
   lblTxtSalaire['fg'] = '#000000'
   lblTxtSalaire['width'] = 20
   lblTxtSalaire['height'] = 2
   lblTxtSalaire['borderwidth'] = 2
   lblTxtSalaire['relief'] = 'groove'
   lblTxtSalaire['font'] = ('Calibri', '12', 'bold')
   lblTxtSalaire.grid(row=0, column=4)

   # - Porchain page
   btnProchain = tk.Button(recherche)
   btnProchain['image'] = imgFlecheDroite
   btnProchain['relief'] = 'flat'
   btnProchain['bg'] = '#ffffff'
   btnProchain['fg'] = '#000000'
   btnProchain['font'] = ('Calibri', '12', 'bold')
   btnProchain['command'] = prochainRecherche
   btnProchain.grid(row=5, column=3, sticky='e')

   # - Page précédente
   btnPrecedent = tk.Button(recherche)
   btnPrecedent['image'] = imgFlecheGauche
   btnPrecedent['relief'] = 'flat'
   btnPrecedent['bg'] = '#ffffff'
   btnPrecedent['fg'] = '#000000'
   btnPrecedent['font'] = ('Calibri', '12', 'bold')
   btnPrecedent['command'] = precedentRecherche
   btnPrecedent.grid(row=5, column=0, sticky='w')

   # - Page
   lblPagee = tk.Label(recherche)
   lblPagee['text'] = 'Page {} sur {}'.format(1,1)
   lblPagee['bg'] = '#ffffff'
   lblPagee['fg'] = '#000000'
   lblPagee['font'] = ('Calibri', '12', 'bold')
   lblPagee.grid(row=5, column=1, columnspan=2)

# - Feneêtre de configuration
def config():
   
   # - Variables globales
   global impotretenu, heurespourbonis, tauxbonis, cadreConfiguration

   # - Création de la fenêtre de configuration
   cadreConfiguration = tk.Toplevel()
   cadreConfiguration['bg'] = arriereplan1
   cadreConfiguration.title("Configuration")
   cadreConfiguration.geometry("500x380")

   # - Titre de la fenêtre
   lblConfiguration = tk.Label(cadreConfiguration)
   lblConfiguration['text'] = "Configuration des variables \n (Valeurs décimales avec un point (ex: 0.5))"
   lblConfiguration['bg'] = arriereplan1
   lblConfiguration['fg'] = '#000000'
   lblConfiguration['font'] = ('Calibri', '12', 'bold')
   lblConfiguration.grid(row=0, column=0, columnspan=2, pady=20, padx=90)

   # - Impôt retenu
   lblimpotretenu = tk.Label(cadreConfiguration)
   lblimpotretenu['text'] = "Impôt retenu"
   lblimpotretenu['bg'] = arriereplan1
   lblimpotretenu['fg'] = '#000000'
   lblimpotretenu['font'] = ('Calibri', '12')
   lblimpotretenu.grid(row=1, column=0, pady=20)

   # - Entrée de l'impôt retenu
   impotretenu = tk.StringVar()
   entlblimpotretenu = tk.Entry(cadreConfiguration)
   entlblimpotretenu['bg'] = boites
   entlblimpotretenu['fg'] = '#000000'
   entlblimpotretenu['textvariable'] = impotretenu
   entlblimpotretenu['font'] = ('Calibri', '12')
   entlblimpotretenu.grid(row=1, column=1, pady=20)

   # - Heures pour bonis
   lblheurespourbonis = tk.Label(cadreConfiguration)
   lblheurespourbonis['text'] = "Heures pour bonis"
   lblheurespourbonis['bg'] = arriereplan1
   lblheurespourbonis['fg'] = '#000000'
   lblheurespourbonis['font'] = ('Calibri', '12')
   lblheurespourbonis.grid(row=2, column=0, pady=20)

   # - Entrée des heures pour bonis
   heurespourbonis = tk.StringVar()
   entlblheurespourbonis = tk.Entry(cadreConfiguration)
   entlblheurespourbonis['bg'] = boites
   entlblheurespourbonis['fg'] = '#000000'
   entlblheurespourbonis['textvariable'] = heurespourbonis
   entlblheurespourbonis['font'] = ('Calibri', '12')
   entlblheurespourbonis.grid(row=2, column=1, pady=20)

   # - Taux de bonis
   lbltauxbonis = tk.Label(cadreConfiguration)
   lbltauxbonis['text'] = "Taux de bonis"
   lbltauxbonis['bg'] = arriereplan1
   lbltauxbonis['fg'] = '#000000'
   lbltauxbonis['font'] = ('Calibri', '12')
   lbltauxbonis.grid(row=3, column=0, pady=20)

   # - Entrée du taux de bonis
   tauxbonis = tk.StringVar()
   entlbltauxbonis = tk.Entry(cadreConfiguration)
   entlbltauxbonis['bg'] = boites
   entlbltauxbonis['fg'] = '#000000'
   entlbltauxbonis['textvariable'] = tauxbonis
   entlbltauxbonis['font'] = ('Calibri', '12')
   entlbltauxbonis.grid(row=3, column=1, pady=20)  

   # - Bouton soumettre
   btnSoumettre = tk.Button(cadreConfiguration)
   btnSoumettre['text'] = "Soumettre"
   btnSoumettre['bg'] = boites
   btnSoumettre['fg'] = '#000000'
   btnSoumettre['font'] = ('Calibri', '12')
   btnSoumettre['command'] = soumettre
   btnSoumettre.grid(row=4, column=0, columnspan=2, pady=20)
   
# - Soumettre les variables pour la configuration
def soumettre():

   # - Variables globales
   global heures_pour_bonis, impot_retenu, bonis, impotretenu, heurespourbonis, tauxbonis

   # - Verifier si les entrées sont remplies
   if impotretenu.get() == "" or heurespourbonis.get() == "" or tauxbonis.get() == "":
      erreur("Remplir toutes les cases ou quitter pour ne pas changer les variables", "Configuration")
   else:
      # - Vérifier si les entrées sont des nombres
      if sinombre(impotretenu.get()) == False:
         erreur("L'impôt retenu doit être un nombre", "Configuration")
      elif sinombre(heurespourbonis.get()) == False:
         erreur("Les heures pour bonis doivent être un nombre", "Configuration")
      elif sinombre(tauxbonis.get()) == False:
         erreur("Le taux de bonis doit être un nombre", "Configuration")
      else:
         try:
            # - Détruire le message d'erreur
            lblErreur.destroy()
         except:
            pass
         # - Assigner les nouvelles variables
         impot_retenu = float(impotretenu.get())
         heures_pour_bonis = float(heurespourbonis.get())
         bonis = float(tauxbonis.get())
         # - Détruire la fenêtre
         cadreConfiguration.destroy()

# - Cadre pour les emplois
def emplois():

   # - Variables globales
   global nomemploi, tauxemploi, emplois
   emplois = tk.Toplevel()
   emplois['bg'] = arriereplan1
   emplois.title("Emplois")
   emplois.geometry("500x380")

   # - Titre
   lblEmplois = tk.Label(emplois)
   lblEmplois['text'] = "Configuration des emplois/postes"
   lblEmplois['bg'] = arriereplan1
   lblEmplois['fg'] = '#000000'
   lblEmplois['font'] = ('Calibri', '12', 'bold')
   lblEmplois.grid(row=0, column=0, columnspan=2, pady=20, padx=130)

   # - Nom de l'emploi
   lblNom = tk.Label(emplois)
   lblNom['text'] = "Nom"
   lblNom['bg'] = arriereplan1
   lblNom['fg'] = '#000000'
   lblNom['font'] = ('Calibri', '12')
   lblNom.grid(row=1, column=0, pady=20)

   # - Entrée du nom de l'emploi
   nomemploi = tk.StringVar()
   entlblNom = tk.Entry(emplois)
   entlblNom['bg'] = boites
   entlblNom['fg'] = '#000000'
   entlblNom['textvariable'] = nomemploi
   entlblNom['font'] = ('Calibri', '12')
   entlblNom.grid(row=1, column=1, pady=20)

   # - Taux de l'emploi
   lblTaux = tk.Label(emplois)
   lblTaux['text'] = "Taux ($/h)"
   lblTaux['bg'] = arriereplan1
   lblTaux['fg'] = '#000000'
   lblTaux['font'] = ('Calibri', '12')
   lblTaux.grid(row=2, column=0, pady=20)

   # - Entrée du taux de l'emploi
   tauxemploi = tk.StringVar()
   entlblTaux = tk.Entry(emplois)
   entlblTaux['bg'] = boites
   entlblTaux['fg'] = '#000000'
   entlblTaux['textvariable'] = tauxemploi
   entlblTaux['font'] = ('Calibri', '12')
   entlblTaux.grid(row=2, column=1, pady=20)

   # - Bouton soumettre
   btnSoumettre = tk.Button(emplois)
   btnSoumettre['text'] = "Ajouter"
   btnSoumettre['bg'] = boites
   btnSoumettre['fg'] = '#000000'
   btnSoumettre['font'] = ('Calibri', '12')
   btnSoumettre['command'] = soumettreEmplois
   btnSoumettre.grid(row=3, column=0, columnspan=2, pady=20)

def soumettreEmplois():

   # - Variables globales
   global nomemploi, tauxemploi, emplois, lblErreur, dropPoste, poste

   # - Vérifier si les entrées sont remplies
   if nomemploi.get() == "" or tauxemploi.get() == "":
      erreur("Remplir toutes les cases ou quitter pour ne pas ajouter des postes", "Preferences")
   else:
      # - Vérifier si les entrées sont des nombres
      if sinombre(tauxemploi.get()) == False:
         erreur("Le taux d'emploi doit être un nombre", "Preferences")
      else:
         try:
            # - Détruire le message d'erreur
            lblErreur.destroy()
         except:
            pass
         # - Ajouter le poste
         postesoptions['{}'.format(nomemploi.get())] = float(tauxemploi.get())

         # - Détruire le menu déroulant
         dropPoste.destroy()

         # - Recréer le menu déroulant
         poste = tk.StringVar()
         poste.set("Poste")
         dropPoste = tk.OptionMenu(cadreEmployersEntry, poste, *postesoptions)
         dropPoste['bg'] = boites
         dropPoste['fg'] = '#000000'
         dropPoste['font'] = ('Calibri', '12')
         dropPoste.grid(row=1, column=2)

# - Vérifier si x est un nombre
def sinombre(x):
   try:
      # - Si oui, retourner True
      float(x)
      return True
   # - Si non, retourner False
   except ValueError:
      return False

# - Message d'erreur
def erreur(message, endroit):

   # - Variables globales
   global lblErreur

   # - Vérifier si le message d'erreur est pour EmployersEntry
   if endroit == "EmployersEntry":
      lblErreur = tk.Label(cadreEmployersEntry)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=3, column=0, columnspan=4, sticky='nsew')

   # - Vérifier si le message d'erreur est pour la fenêtre Recherche
   elif endroit == "Recherche":
      lblErreur = tk.Label(cadreRecherche)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=2, column=0, columnspan=3, sticky='nsew')

   # - Vérifier si le message d'erreur est pour la fenêtre Configuration
   elif endroit == "Configuration":
      lblErreur = tk.Label(cadreConfiguration)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=5, column=0, columnspan=3, sticky='nsew')

   # - Vérifier si le message d'erreur est pour la fenêtre Preferences
   elif endroit == "Preferences":
      lblErreur = tk.Label(emplois)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=5, column=0, columnspan=2, sticky='nsew')
   
   # - Si endroit n'est pas un endroit valide, passer
   else:
      pass

# - Fenetre
def cadre():

   # - Variables globales
   global lblTxttNom, lblTxttPrenom, lblTxttHeures, lblTxttSalaire, lblTxttPoste, entNom, entPrenom, entHeures, lblPage, nom, prenom, heures, poste, fenetre, cadreEmployersEntry, cadreEmployers, imgFlecheDroite, imgFlecheGauche, dropPoste
   
   # - Fenetre
   fenetre = tk.Tk()
   fenetre.title("Comptabilité")
   fenetre.geometry("830x740")
   fenetre['bg'] = '#ffffff'

   # - Configuration de la fenetre
   fenetre.columnconfigure(0, weight=1)
   fenetre.columnconfigure(1, weight=1)
   fenetre.columnconfigure(2, weight=1)
   fenetre.columnconfigure(3, weight=1)
   fenetre.rowconfigure(0, weight=1)
   fenetre.rowconfigure(1, weight=1)
   fenetre.rowconfigure(2, weight=1)
   fenetre.rowconfigure(3, weight=1)
   fenetre.rowconfigure(4, weight=1)

   # - Menus
   mnuBarreMenu = tk.Menu(fenetre)
   fenetre['menu'] = mnuBarreMenu

   # - Menu Fichier
   mnuFichier = tk.Menu(mnuBarreMenu, tearoff=0)
   mnuBarreMenu.add_cascade(label="Fichier", menu=mnuFichier)
   mnuFichier.add_command(label="Quitter", command=fenetre.destroy)

   # - Menu Options
   mnuOptions = tk.Menu(mnuBarreMenu, tearoff=0)
   mnuBarreMenu.add_cascade(label="Options", menu=mnuOptions)
   mnuOptions.add_command(label="Configuration", command=config)
   mnuOptions.add_command(label="Emplois", command=emplois)

   # - images
   imgFlecheGauche = tk.PhotoImage(file="flechegauche.gif")
   imgFlecheDroite = tk.PhotoImage(file="flechedroite.gif")
   imgLoupe = tk.PhotoImage(file="loupe.gif")

   # - Cadres

   # - Cadre Employers
   cadreEmployers = tk.Frame(fenetre)
   cadreEmployers['bg'] = '#ffffff'
   cadreEmployers.grid(row=1, column=0, rowspan=4, columnspan=4, sticky='nsew')

   # - Éviter que le cadre Employers change de taille
   cadreEmployers.grid_propagate(0)

   # - Cadre EmployersEntry
   cadreEmployersEntry = tk.Frame(fenetre)
   cadreEmployersEntry['bg'] = arriereplan1
   cadreEmployersEntry.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='nsew')

   # - Bouton sur clavier pour ajouter un employer
   fenetre.bind("<Return>", lambda x: ajouter())

   # - Cadre EmployersEntry configuration
   cadreEmployersEntry.columnconfigure(0, weight=1)
   cadreEmployersEntry.columnconfigure(1, weight=1)
   cadreEmployersEntry.columnconfigure(2, weight=1)
   cadreEmployersEntry.columnconfigure(3, weight=1)
   cadreEmployersEntry.rowconfigure(0, weight=1)
   cadreEmployersEntry.rowconfigure(1, weight=1)
   cadreEmployersEntry.rowconfigure(2, weight=1)

   # - Nom
   lblNom = tk.Label(cadreEmployersEntry)
   lblNom['text'] = 'Nom'
   lblNom['bg'] = arriereplan1
   lblNom['fg'] = '#000000'
   lblNom['font'] = ('Calibri', '12', 'bold')
   lblNom.grid(row=0, column=0)

   # - Prenom
   lblPrenom = tk.Label(cadreEmployersEntry)
   lblPrenom['text'] = 'Prénom'
   lblPrenom['bg'] = arriereplan1
   lblPrenom['fg'] = '#000000'
   lblPrenom['font'] = ('Calibri', '12', 'bold')
   lblPrenom.grid(row=0, column=1)

   # - Poste
   lblPoste = tk.Label(cadreEmployersEntry)
   lblPoste['text'] = 'Poste'
   lblPoste['bg'] = arriereplan1
   lblPoste['fg'] = '#000000'
   lblPoste['font'] = ('Calibri', '12', 'bold')
   lblPoste.grid(row=0, column=2)

   # - Heures
   lblHeures = tk.Label(cadreEmployersEntry)
   lblHeures['text'] = 'Heures'
   lblHeures['bg'] = arriereplan1
   lblHeures['fg'] = '#000000'
   lblHeures['font'] = ('Calibri', '12', 'bold')
   lblHeures.grid(row=0, column=3)

   # - Entrée nom
   nom = tk.StringVar()
   entNom = tk.Entry(cadreEmployersEntry)
   entNom['bg'] = boites
   entNom['fg'] = '#000000'
   entNom['font'] = ('Calibri', '12')
   entNom['textvariable'] = nom
   entNom.grid(row=1, column=0)

   # - Entrée prénom
   prenom = tk.StringVar()
   entPrenom = tk.Entry(cadreEmployersEntry)
   entPrenom['bg'] = boites
   entPrenom['fg'] = '#000000'
   entPrenom['font'] = ('Calibri', '12')
   entPrenom['textvariable'] = prenom
   entPrenom.grid(row=1, column=1)

   # - Entrée poste
   poste = tk.StringVar()
   poste.set("Poste")
   dropPoste = tk.OptionMenu(cadreEmployersEntry, poste, *postesoptions)
   dropPoste['bg'] = boites
   dropPoste['fg'] = '#000000'
   dropPoste['font'] = ('Calibri', '12')
   dropPoste.grid(row=1, column=2)

   # - Entrée heures
   heures = tk.StringVar()
   entHeures = tk.Entry(cadreEmployersEntry)
   entHeures['bg'] = boites
   entHeures['fg'] = '#000000'
   entHeures['font'] = ('Calibri', '12')
   entHeures['textvariable'] = heures
   entHeures.grid(row=1, column=3)

   # - Bouton ajouter
   btnAjouter = tk.Button(cadreEmployersEntry)
   btnAjouter['text'] = 'Ajouter'
   btnAjouter['bg'] = boites
   btnAjouter['fg'] = '#000000'
   btnAjouter['font'] = ('Calibri', '12', 'bold')
   btnAjouter['command'] = ajouter
   btnAjouter.grid(row=2, column=1)

   # - Bouton pour rechercher
   btnRechercher = tk.Button(cadreEmployersEntry)
   btnRechercher['image'] = imgLoupe
   btnRechercher['relief'] = 'flat'
   btnRechercher['bg'] = '#ffffff'
   btnRechercher['fg'] = '#000000'
   btnRechercher['font'] = ('Calibri', '12', 'bold')
   btnRechercher['command'] = popupRecherche
   btnRechercher.grid(row=2, column=2)

   # - Pages

   # - Porchain page
   btnProchain = tk.Button(fenetre)
   btnProchain['image'] = imgFlecheDroite
   btnProchain['relief'] = 'flat'
   btnProchain['bg'] = '#ffffff'
   btnProchain['fg'] = '#000000'
   btnProchain['font'] = ('Calibri', '12', 'bold')
   btnProchain['command'] = prochain
   btnProchain.grid(row=5, column=3, sticky='e')

   # - Page précédente
   btnPrecedent = tk.Button(fenetre)
   btnPrecedent['image'] = imgFlecheGauche
   btnPrecedent['relief'] = 'flat'
   btnPrecedent['bg'] = '#ffffff'
   btnPrecedent['fg'] = '#000000'
   btnPrecedent['font'] = ('Calibri', '12', 'bold')
   btnPrecedent['command'] = precedent
   btnPrecedent.grid(row=5, column=0, sticky='w')

   # - Page
   lblPage = tk.Label(fenetre)
   lblPage['text'] = 'Page {} sur {}'.format(1,1)
   lblPage['bg'] = '#ffffff'
   lblPage['fg'] = '#000000'
   lblPage['font'] = ('Calibri', '12', 'bold')
   lblPage.grid(row=5, column=1, columnspan=2)

   # - Cadre Employers

   # - Nom
   lblTxttNom = tk.Label(cadreEmployers)
   lblTxttNom['text'] = 'Nom'
   lblTxttNom['bg'] = arriereplan2
   lblTxttNom['fg'] = '#000000'
   lblTxttNom['width'] = 20
   lblTxttNom['height'] = 2
   lblTxttNom['borderwidth'] = 2
   lblTxttNom['relief'] = 'groove'
   lblTxttNom['font'] = ('Calibri', '12', 'bold')
   lblTxttNom.grid(row=0, column=0)

   # - Prénom
   lblTxttPrenom = tk.Label(cadreEmployers)
   lblTxttPrenom['text'] = 'Prénom'
   lblTxttPrenom['bg'] = arriereplan2
   lblTxttPrenom['fg'] = '#000000'
   lblTxttPrenom['width'] = 20
   lblTxttPrenom['height'] = 2
   lblTxttPrenom['borderwidth'] = 2
   lblTxttPrenom['relief'] = 'groove'
   lblTxttPrenom['font'] = ('Calibri', '12', 'bold')
   lblTxttPrenom.grid(row=0, column=1)

   # - Poste
   lblTxttPoste = tk.Label(cadreEmployers)
   lblTxttPoste['text'] = 'Poste'
   lblTxttPoste['bg'] = arriereplan2
   lblTxttPoste['fg'] = '#000000'
   lblTxttPoste['width'] = 20
   lblTxttPoste['height'] = 2
   lblTxttPoste['borderwidth'] = 2
   lblTxttPoste['relief'] = 'groove'
   lblTxttPoste['font'] = ('Calibri', '12', 'bold')
   lblTxttPoste.grid(row=0, column=2)

   # - Heures
   lblTxttHeures = tk.Label(cadreEmployers)
   lblTxttHeures['text'] = 'Heures'
   lblTxttHeures['bg'] = arriereplan2
   lblTxttHeures['fg'] = '#000000'
   lblTxttHeures['width'] = 20
   lblTxttHeures['height'] = 2
   lblTxttHeures['borderwidth'] = 2
   lblTxttHeures['relief'] = 'groove'
   lblTxttHeures['font'] = ('Calibri', '12', 'bold')
   lblTxttHeures.grid(row=0, column=3)

   # - Salaire
   lblTxttSalaire = tk.Label(cadreEmployers)
   lblTxttSalaire['text'] = 'Salaire'
   lblTxttSalaire['bg'] = arriereplan2
   lblTxttSalaire['fg'] = '#000000'
   lblTxttSalaire['width'] = 20
   lblTxttSalaire['height'] = 2
   lblTxttSalaire['borderwidth'] = 2
   lblTxttSalaire['relief'] = 'groove'
   lblTxttSalaire['font'] = ('Calibri', '12', 'bold')
   lblTxttSalaire.grid(row=0, column=4)

   # - Montrer les instructions au début
   instructions()

   # - Afficher la fenêtre
   fenetre.mainloop()

# - Instructions
def instructions():

   # - Cadre Instructions
   cadreInstructions = tk.Frame(fenetre)
   cadreInstructions['bg'] = arriereplan1
   cadreInstructions.grid(row=0, column=0, rowspan=6, columnspan=4, sticky='nsew')

   # - Instructions titre
   lblInstructions = tk.Label(cadreInstructions)
   lblInstructions['text'] = 'Instructions'
   lblInstructions['bg'] = arriereplan1
   lblInstructions['fg'] = '#000000'
   lblInstructions['font'] = ('Calibri', '20', 'bold')
   lblInstructions.grid(row=0, column=0, sticky='nsew', pady = 30, padx=340)

   # - Instructions
   lblComment = tk.Label(cadreInstructions)
   lblComment['text'] = 'Bienvenue à un programme de comptabilité pour restaurants. Ce programme est capable de calculer le salaire de \nchaque employé, ainsi que le bonis qui doit y être ajouté, selon le nombre d\'heures travaillées et quel poste l\'employé a.\n Par défaut le programme calcule le salaire avec un import retenu sur le salaire de {} %, {} heures de travail \npour reçevoir un bonis de {} % sur le salaire. \n(Ces options peuvent être configurés dans le programme via le menu de configuration).\n\n Les options d\'emplois peuvent être configurées via le menu d\'emplois. '.format(impot_retenu*100, heures_pour_bonis, bonis)
   lblComment['bg'] = arriereplan1
   lblComment['fg'] = '#000000'
   lblComment['font'] = ('Calibri', '12')
   lblComment.grid(row=1, column=0, sticky='nsew', pady = 20)

   # - Bouton pour fermer le cadre
   btnFermer = tk.Button(cadreInstructions)
   btnFermer['text'] = 'Continuer'
   btnFermer['bg'] = '#ffffff'
   btnFermer['fg'] = '#000000'
   btnFermer['font'] = ('Calibri', '12', 'bold')
   btnFermer['command'] = cadreInstructions.destroy
   btnFermer.grid(row=2, column=0, pady=20)

# - Fonctions pour cadre

# - Montrer les résultats
def update(x):

   # - Variables globales
   global employes, groupes, page_courant, employesTrouves, cadreRecherche, cadreResultat, page_courant_recherche, groupesrecherche

   # - Si x est égal à "recherche", alors on affiche les résultats de la recherche
   if x == "recherche": 

      # - Détruire les anciens résultats
      for i in cadreResultat.winfo_children():
         if i != lblTxtNom and i != lblTxtPrenom and i != lblTxtPoste and i != lblTxtHeures and i != lblTxtSalaire: 
            i.destroy()
         else:
            pass

      # - Afficher la page courante
      updatePage("Recherche")

      # - Afficher les résultats pour chaque employé trouvé
      groupe_courant = groupesrecherche[page_courant_recherche-1]
      for i, trouve in enumerate(groupe_courant):

         # - Nom
         lblPersonne = tk.Label(cadreResultat)
         lblPersonne['text'] = trouve["nom"]
         lblPersonne['bg'] = '#ffffff'
         lblPersonne['fg'] = '#000000'
         lblPersonne['relief'] = 'groove'
         lblPersonne['width'] = 20
         lblPersonne['height'] = 2
         lblPersonne['font'] = ('Calibri', '12')
         lblPersonne.grid(row=i+1, column=0)

         # - Prénom
         lblPrenom = tk.Label(cadreResultat)
         lblPrenom['text'] = trouve["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Calibri', '12')
         lblPrenom.grid(row=i+1, column=1)

         # - Poste
         lblPoste = tk.Label(cadreResultat)
         lblPoste['text'] = trouve["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Calibri', '12')
         lblPoste.grid(row=i+1, column=2)

         # - Heures
         lblHeures = tk.Label(cadreResultat)
         lblHeures['text'] = trouve["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Calibri', '12')
         lblHeures.grid(row=i+1, column=3)

         # - Salaire
         lblSalaire = tk.Label(cadreResultat)
         lblSalaire['text'] = "$ {:.2f}".format(trouve["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Calibri', '12')
         lblSalaire.grid(row=i+1, column=4)

   # - Sinon, on affiche les résultats normaux dans le cadre Employers
   else:

      # - Détruire les anciens résultats
      for i in cadreEmployers.winfo_children():
         if i != lblTxttNom and i != lblTxttPrenom and i != lblTxttPoste and i != lblTxttHeures and i != lblTxttSalaire:
            i.destroy()
         else:
            pass
      
      # - Afficher la page courante
      updatePage("Ajout")

      # - Afficher les résultats pour chaque employé
      groupe_courant = groupes[page_courant-1]
      for i, employe in enumerate(groupe_courant):

         # - Nom
         lblPersonne = tk.Label(cadreEmployers)
         lblPersonne['text'] = employe["nom"]
         lblPersonne['bg'] = '#ffffff'
         lblPersonne['fg'] = '#000000'
         lblPersonne['relief'] = 'groove'
         lblPersonne['width'] = 20
         lblPersonne['height'] = 2
         lblPersonne['font'] = ('Calibri', '12')
         lblPersonne.grid(row=i+1, column=0)

         # - Prénom
         lblPrenom = tk.Label(cadreEmployers)
         lblPrenom['text'] = employe["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Calibri', '12')
         lblPrenom.grid(row=i+1, column=1)

         # - Poste
         lblPoste = tk.Label(cadreEmployers)
         lblPoste['text'] = employe["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Calibri', '12')
         lblPoste.grid(row=i+1, column=2)

         # - Heures
         lblHeures = tk.Label(cadreEmployers)
         lblHeures['text'] = employe["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Calibri', '12')
         lblHeures.grid(row=i+1, column=3)

         # - Salaire
         lblSalaire = tk.Label(cadreEmployers)
         lblSalaire['text'] = "$ {:.2f}".format(employe["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Calibri', '12')
         lblSalaire.grid(row=i+1, column=4)


# - Commencer le programme en affichant la feneêtre principale avec la page d'accueil
cadre()