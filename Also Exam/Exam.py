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

#ADD BONUSESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

# - Programme principal ------------------------------------------------------------------------------------------

# - Variables
TEST = True
rows = 0
entreesParPage = 10
page_courant = 1
employes = []
groupes = []
postesoptions = {
   'Cuisinier' : 19.00,
   'Serveur' : 15.50,
   'Plongeur' : 28.98,
   'Caissier' : 15.98
}
impot_retenu = 0.105  #10,5% de retenu sur le salaire
heures_pour_bonis = 160
bonis = 5
types = ["Nom", "Prenom", "Poste", "Heures", "Salaire"]
employesTrouves = []
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
   global employes, postesoptions, rows, TEST

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
            rows += 1
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
            grouper()
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
def grouper():
   # - Variables globales
   global entreesParPage, employes, groupes
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

def updatePage():
      global page_courant, groupes
      lblPage['text'] = "Page {} sur {}".format(page_courant, len(groupes))

def prochain():
   global page_courant, groupes
   nombreGroupes = len(groupes)
   if page_courant < nombreGroupes:
      page_courant += 1
      update("Ajout")

def precedent():
   global page_courant, groupes
   if page_courant > 1:
      page_courant -= 1
      update("Ajout")

def search():
    global typeRecherche, motcle, employesTrouves, lblErreur
    try: 
        lblErreur.destroy()
    except:
        pass
    employesTrouves.clear()
    if motcle.get() and typeRecherche.get():
        recherche = motcle.get()
        typeSearch = typeRecherche.get()
        if sinombre(recherche) == True:
            for i in employes:
                if float(recherche) == float(i[typeSearch.lower()]):
                    employesTrouves.append(i)
                else:
                    pass
        else:
            for i in employes:
                if recherche.lower() in str(i[typeSearch.lower()]).lower():
                    employesTrouves.append(i)
                else:
                    pass
        
        if len(employesTrouves) == 0:
            erreur("Aucun résultat trouvé", "Recherche")
        else:
            update("recherche")
    else:
        erreur("Veuillez remplir tous les champs", "Recherche")


def popupRecherche():
   global typeRecherche, motcle, recherche, lblErreur, cadreRecherche, cadreResultat, lblTxtNom, lblTxtPrenom, lblTxtPoste, lblTxtHeures, lblTxtSalaire
   cadreRecherche = tk.Toplevel()
   cadreRecherche.title("Rechercher")
   cadreRecherche.geometry("830x500")
   cadreRecherche['bg'] = arriereplan1

   cadreResultat = tk.Frame(cadreRecherche)
   cadreResultat['bg'] = '#ffffff'
   cadreResultat.grid(row = 3, column=0, columnspan=4, sticky='nsew')

   lblRecherche = tk.Label(cadreRecherche)
   lblRecherche['text'] = "Rechercher"
   lblRecherche['bg'] = arriereplan1
   lblRecherche['fg'] = '#000000'
   lblRecherche['font'] = ('Calibri', '12', 'bold')
   lblRecherche.grid(row=0, column=0, pady=5)

   lblType = tk.Label(cadreRecherche)
   lblType['text'] = "Type de recherche"
   lblType['bg'] = arriereplan1
   lblType['fg'] = '#000000'
   lblType['font'] = ('Calibri', '12', 'bold')
   lblType.grid(row=0, column=1)

   lblErreur = tk.Label(cadreRecherche)
   lblErreur['text'] = ""
   lblErreur['bg'] = arriereplan1
   lblErreur['fg'] = '#ff0000'
   lblErreur['font'] = ('Calibri', '12', 'bold')
   lblErreur.grid(row=0, column=3)

   motcle = tk.StringVar()
   entRecherche = tk.Entry(cadreRecherche)
   entRecherche['bg'] = boites
   entRecherche['fg'] = '#000000'
   entRecherche['textvariable'] = motcle
   entRecherche['font'] = ('Calibri', '12')
   entRecherche.grid(row=1, column=0)

   typeRecherche = tk.StringVar()
   typeRecherche.set("Nom")
   dropType = tk.OptionMenu(cadreRecherche, typeRecherche, *types)
   dropType['bg'] = boites
   dropType['fg'] = '#000000'
   dropType['font'] = ('Calibri', '12')
   dropType.grid(row=1, column=1)

   btnRechercher = tk.Button(cadreRecherche)
   btnRechercher['text'] = "Rechercher"
   btnRechercher['bg'] = boites
   btnRechercher['fg'] = '#000000'
   btnRechercher['font'] = ('Calibri', '12', 'bold')
   btnRechercher['command'] = search
   btnRechercher.grid(row=1, column=2, pady=20)

   lblTxtNom = tk.Label(cadreResultat)
   lblTxtNom['text'] = 'Nom'
   lblTxtNom['bg'] = arriereplan2
   lblTxtNom['fg'] = '#000000'
   lblTxtNom['width'] = 20
   lblTxtNom['height'] = 2
   lblTxtNom['borderwidth'] = 2
   lblTxtNom['relief'] = 'groove'
   lblTxtNom['font'] = ('Calibri', '12')
   lblTxtNom.grid(row=0, column=0)

   lblTxtPrenom = tk.Label(cadreResultat)
   lblTxtPrenom['text'] = 'Prénom'
   lblTxtPrenom['bg'] = arriereplan2
   lblTxtPrenom['fg'] = '#000000'
   lblTxtPrenom['width'] = 20
   lblTxtPrenom['height'] = 2
   lblTxtPrenom['borderwidth'] = 2
   lblTxtPrenom['relief'] = 'groove'
   lblTxtPrenom['font'] = ('Calibri', '12')
   lblTxtPrenom.grid(row=0, column=1)

   lblTxtPoste = tk.Label(cadreResultat)
   lblTxtPoste['text'] = 'Poste'
   lblTxtPoste['bg'] = arriereplan2
   lblTxtPoste['fg'] = '#000000'
   lblTxtPoste['width'] = 20
   lblTxtPoste['height'] = 2
   lblTxtPoste['borderwidth'] = 2
   lblTxtPoste['relief'] = 'groove'
   lblTxtPoste['font'] = ('Calibri', '12')
   lblTxtPoste.grid(row=0, column=2)

   lblTxtHeures = tk.Label(cadreResultat)
   lblTxtHeures['text'] = 'Heures'
   lblTxtHeures['bg'] = arriereplan2
   lblTxtHeures['fg'] = '#000000'
   lblTxtHeures['width'] = 20
   lblTxtHeures['height'] = 2
   lblTxtHeures['borderwidth'] = 2
   lblTxtHeures['relief'] = 'groove'
   lblTxtHeures['font'] = ('Calibri', '12')
   lblTxtHeures.grid(row=0, column=3)

   lblTxtSalaire = tk.Label(cadreResultat)
   lblTxtSalaire['text'] = 'Salaire'
   lblTxtSalaire['bg'] = arriereplan2
   lblTxtSalaire['fg'] = '#000000'
   lblTxtSalaire['width'] = 20
   lblTxtSalaire['height'] = 2
   lblTxtSalaire['borderwidth'] = 2
   lblTxtSalaire['relief'] = 'groove'
   lblTxtSalaire['font'] = ('Calibri', '12')
   lblTxtSalaire.grid(row=0, column=4)

def config():
   global impotretenu, heurespourbonis, tauxbonis, cadreConfiguration
   cadreConfiguration = tk.Toplevel()
   cadreConfiguration['bg'] = arriereplan1
   cadreConfiguration.title("Configuration")
   cadreConfiguration.geometry("500x370")

   lblConfiguration = tk.Label(cadreConfiguration)
   lblConfiguration['text'] = "Configuration des variables \n (Valeurs décimales avec un point (ex: 0.5))"
   lblConfiguration['bg'] = arriereplan1
   lblConfiguration['fg'] = '#000000'
   lblConfiguration['font'] = ('Calibri', '12', 'bold')
   lblConfiguration.grid(row=0, column=0, columnspan=2, pady=20, padx=90)

   lblimpotretenu = tk.Label(cadreConfiguration)
   lblimpotretenu['text'] = "Impôt retenu"
   lblimpotretenu['bg'] = arriereplan1
   lblimpotretenu['fg'] = '#000000'
   lblimpotretenu['font'] = ('Calibri', '12')
   lblimpotretenu.grid(row=1, column=0, pady=20)

   impotretenu = tk.StringVar()
   entlblimpotretenu = tk.Entry(cadreConfiguration)
   entlblimpotretenu['bg'] = boites
   entlblimpotretenu['fg'] = '#000000'
   entlblimpotretenu['textvariable'] = impotretenu
   entlblimpotretenu['font'] = ('Calibri', '12')
   entlblimpotretenu.grid(row=1, column=1, pady=20)

   lblheurespourbonis = tk.Label(cadreConfiguration)
   lblheurespourbonis['text'] = "Heures pour bonis"
   lblheurespourbonis['bg'] = arriereplan1
   lblheurespourbonis['fg'] = '#000000'
   lblheurespourbonis['font'] = ('Calibri', '12')
   lblheurespourbonis.grid(row=2, column=0, pady=20)

   heurespourbonis = tk.StringVar()
   entlblheurespourbonis = tk.Entry(cadreConfiguration)
   entlblheurespourbonis['bg'] = boites
   entlblheurespourbonis['fg'] = '#000000'
   entlblheurespourbonis['textvariable'] = heurespourbonis
   entlblheurespourbonis['font'] = ('Calibri', '12')
   entlblheurespourbonis.grid(row=2, column=1, pady=20)

   lbltauxbonis = tk.Label(cadreConfiguration)
   lbltauxbonis['text'] = "Taux de bonis"
   lbltauxbonis['bg'] = arriereplan1
   lbltauxbonis['fg'] = '#000000'
   lbltauxbonis['font'] = ('Calibri', '12')
   lbltauxbonis.grid(row=3, column=0, pady=20)

   tauxbonis = tk.StringVar()
   entlbltauxbonis = tk.Entry(cadreConfiguration)
   entlbltauxbonis['bg'] = boites
   entlbltauxbonis['fg'] = '#000000'
   entlbltauxbonis['textvariable'] = tauxbonis
   entlbltauxbonis['font'] = ('Calibri', '12')
   entlbltauxbonis.grid(row=3, column=1, pady=20)  

   btnSoumettre = tk.Button(cadreConfiguration)
   btnSoumettre['text'] = "Soumettre"
   btnSoumettre['bg'] = boites
   btnSoumettre['fg'] = '#000000'
   btnSoumettre['font'] = ('Calibri', '12')
   btnSoumettre['command'] = soumettre
   btnSoumettre.grid(row=4, column=0, columnspan=2, pady=20)
   

def soumettre():
   global heures_pour_bonis, impot_retenu, bonis, impotretenu, heurespourbonis, tauxbonis

   if sinombre(impotretenu.get()) == False:
      erreur("L'impôt retenu doit être un nombre", "Configuration")
   elif sinombre(heurespourbonis.get()) == False:
      erreur("Les heures pour bonis doivent être un nombre", "Configuration")
   elif sinombre(tauxbonis.get()) == False:
      erreur("Le taux de bonis doit être un nombre", "Configuration")
   else:
      try:
         lblErreur.destroy()
      except:
         pass
      impot_retenu = float(impotretenu.get())
      heures_pour_bonis = float(heurespourbonis.get())
      bonis = float(tauxbonis.get())
      cadreConfiguration.destroy()

def pref():
   global cadrePref, couleur, couleur2, boite
   cadrePref = tk.Toplevel()
   cadrePref['bg'] = arriereplan1
   cadrePref.title("Préférences")
   cadrePref.geometry("600x380")

   lblPref = tk.Label(cadrePref)
   lblPref['text'] = "Préférences \n(Utiliser des codes hexadécimaux (ex: #000000)\n(Cliquer sur soummetre recommencera le programme))"
   lblPref['bg'] = arriereplan1
   lblPref['fg'] = '#000000'
   lblPref['font'] = ('Calibri', '12', 'bold')
   lblPref.grid(row=0, column=0, columnspan=2, pady=20, padx=100)

   lblCouleur = tk.Label(cadrePref)
   lblCouleur['text'] = "Couleur de l'arrière-plan"
   lblCouleur['bg'] = arriereplan1
   lblCouleur['fg'] = '#000000'
   lblCouleur['font'] = ('Calibri', '12')
   lblCouleur.grid(row=1, column=0, pady=20)

   couleur = tk.StringVar()
   entCouleur = tk.Entry(cadrePref)
   entCouleur['bg'] = boites
   entCouleur['fg'] = '#000000'
   entCouleur['textvariable'] = couleur
   entCouleur['font'] = ('Calibri', '12')
   entCouleur.grid(row=1, column=1, pady=20)

   lblCouleur2 = tk.Label(cadrePref)
   lblCouleur2['text'] = "Couleur des cellules"
   lblCouleur2['bg'] = arriereplan1
   lblCouleur2['fg'] = '#000000'
   lblCouleur2['font'] = ('Calibri', '12')
   lblCouleur2.grid(row=2, column=0, pady=20)

   couleur2 = tk.StringVar()
   entCouleur2 = tk.Entry(cadrePref)
   entCouleur2['bg'] = boites
   entCouleur2['fg'] = '#000000'
   entCouleur2['textvariable'] = couleur2
   entCouleur2['font'] = ('Calibri', '12')
   entCouleur2.grid(row=2, column=1, pady=20)

   boite = tk.StringVar()
   lblBoite = tk.Label(cadrePref)
   lblBoite['text'] = "Couleur des bouttons"
   lblBoite['bg'] = arriereplan1
   lblBoite['fg'] = '#000000'
   lblBoite['font'] = ('Calibri', '12')
   lblBoite.grid(row=3, column=0, pady=20)

   entBoite = tk.Entry(cadrePref)
   entBoite['bg'] = boites
   entBoite['fg'] = '#000000'
   entBoite['textvariable'] = boite
   entBoite['font'] = ('Calibri', '12')
   entBoite.grid(row=3, column=1, pady=20)

   btnSoumettrePref = tk.Button(cadrePref)
   btnSoumettrePref['text'] = "Soumettre"
   btnSoumettrePref['bg'] = boites
   btnSoumettrePref['fg'] = '#000000'
   btnSoumettrePref['font'] = ('Calibri', '12')
   btnSoumettrePref['command'] = soumettrePref
   btnSoumettrePref.grid(row=4, column=0, columnspan=2, pady=20)


def soumettrePref():
   global arriereplan1, arriereplan2, boites, cadreResultat, cadrePref, cadreEmployers, cadreEmployersEntry, cadreConfiguration
   arriereplan1 = couleur.get()
   arriereplan2 = couleur2.get()
   boites = boite.get()
   fenetre.destroy()
   cadre()
   update()
   


def sinombre(x):
   try:
      float(x)
      return True
   except ValueError:
      return False



def erreur(message, endroit):
   global lblErreur

   if endroit == "EmployersEntry":
      lblErreur = tk.Label(cadreEmployersEntry)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=3, column=0, columnspan=4, sticky='nsew')
   elif endroit == "Recherche":
      lblErreur = tk.Label(cadreRecherche)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=2, column=0, columnspan=3, sticky='nsew')
   elif endroit == "Configuration":
      lblErreur = tk.Label(cadreConfiguration)
      lblErreur['text'] = message
      lblErreur['bg'] = arriereplan1
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Calibri', '12', 'bold')
      lblErreur.grid(row=5, column=0, columnspan=3, sticky='nsew')
   else:
      pass

def cadre():
   global lblTxttNom, lblTxttPrenom, lblTxttHeures, lblTxttSalaire, lblTxttPoste, entNom, entPrenom, entHeures, lblPage, nom, prenom, heures, poste, fenetre, cadreEmployersEntry, cadreEmployers
   # - Fenetre
   fenetre = tk.Tk()
   fenetre.title("Comptabilité")
   fenetre.geometry("830x740")
   fenetre['bg'] = '#ffffff'

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

   mnuFichier = tk.Menu(mnuBarreMenu, tearoff=0)
   mnuBarreMenu.add_cascade(label="Fichier", menu=mnuFichier)
   mnuFichier.add_command(label="Quitter", command=fenetre.destroy)

   mnuOptions = tk.Menu(mnuBarreMenu, tearoff=0)

   mnuBarreMenu.add_cascade(label="Options", menu=mnuOptions)
   mnuOptions.add_command(label="Configuration", command=config)
   mnuOptions.add_command(label="Préférences", command=pref)

   # - images
   imgFlecheGauche = tk.PhotoImage(file="flechegauche.gif")
   imgFlecheDroite = tk.PhotoImage(file="flechedroite.gif")
   imgLoupe = tk.PhotoImage(file="loupe.gif")

   # - Cadres
   cadreEmployers = tk.Frame(fenetre)
   cadreEmployers['bg'] = '#ffffff'
   cadreEmployers.grid(row=1, column=0, rowspan=4, columnspan=4, sticky='nsew')
   cadreEmployers.grid_propagate(0)

   cadreEmployersEntry = tk.Frame(fenetre)
   cadreEmployersEntry['bg'] = arriereplan1
   cadreEmployersEntry.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='nsew')

   # - Bind
   fenetre.bind("<Return>", lambda x: ajouter())

   # - Cadre EmployersEntry
   cadreEmployersEntry.columnconfigure(0, weight=1)
   cadreEmployersEntry.columnconfigure(1, weight=1)
   cadreEmployersEntry.columnconfigure(2, weight=1)
   cadreEmployersEntry.columnconfigure(3, weight=1)
   cadreEmployersEntry.rowconfigure(0, weight=1)
   cadreEmployersEntry.rowconfigure(1, weight=1)
   cadreEmployersEntry.rowconfigure(2, weight=1)

   lblNom = tk.Label(cadreEmployersEntry)
   lblNom['text'] = 'Nom'
   lblNom['bg'] = arriereplan1
   lblNom['fg'] = '#000000'
   lblNom['font'] = ('Calibri', '12', 'bold')
   lblNom.grid(row=0, column=0)

   lblPrenom = tk.Label(cadreEmployersEntry)
   lblPrenom['text'] = 'Prénom'
   lblPrenom['bg'] = arriereplan1
   lblPrenom['fg'] = '#000000'
   lblPrenom['font'] = ('Calibri', '12', 'bold')
   lblPrenom.grid(row=0, column=1)

   lblPoste = tk.Label(cadreEmployersEntry)
   lblPoste['text'] = 'Poste'
   lblPoste['bg'] = arriereplan1
   lblPoste['fg'] = '#000000'
   lblPoste['font'] = ('Calibri', '12', 'bold')
   lblPoste.grid(row=0, column=2)

   lblHeures = tk.Label(cadreEmployersEntry)
   lblHeures['text'] = 'Heures'
   lblHeures['bg'] = arriereplan1
   lblHeures['fg'] = '#000000'
   lblHeures['font'] = ('Calibri', '12', 'bold')
   lblHeures.grid(row=0, column=3)

   nom = tk.StringVar()
   entNom = tk.Entry(cadreEmployersEntry)
   entNom['bg'] = boites
   entNom['fg'] = '#000000'
   entNom['font'] = ('Calibri', '12')
   entNom['textvariable'] = nom
   entNom.grid(row=1, column=0)

   prenom = tk.StringVar()
   entPrenom = tk.Entry(cadreEmployersEntry)
   entPrenom['bg'] = boites
   entPrenom['fg'] = '#000000'
   entPrenom['font'] = ('Calibri', '12')
   entPrenom['textvariable'] = prenom
   entPrenom.grid(row=1, column=1)

   poste = tk.StringVar()
   poste.set("Poste")
   dropPoste = tk.OptionMenu(cadreEmployersEntry, poste, *postesoptions)
   dropPoste['bg'] = boites
   dropPoste['fg'] = '#000000'
   dropPoste['font'] = ('Calibri', '12')
   dropPoste.grid(row=1, column=2)

   heures = tk.StringVar()
   entHeures = tk.Entry(cadreEmployersEntry)
   entHeures['bg'] = boites
   entHeures['fg'] = '#000000'
   entHeures['font'] = ('Calibri', '12')
   entHeures['textvariable'] = heures
   entHeures.grid(row=1, column=3)

   btnAjouter = tk.Button(cadreEmployersEntry)
   btnAjouter['text'] = 'Ajouter'
   btnAjouter['bg'] = boites
   btnAjouter['fg'] = '#000000'
   btnAjouter['font'] = ('Calibri', '12', 'bold')
   btnAjouter['command'] = ajouter
   btnAjouter.grid(row=2, column=1)

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

   lblPage = tk.Label(fenetre)
   lblPage['text'] = 'Page {} sur {}'.format(1,1)
   lblPage['bg'] = '#ffffff'
   lblPage['fg'] = '#000000'
   lblPage['font'] = ('Calibri', '12', 'bold')
   lblPage.grid(row=5, column=1, columnspan=2)


   # - Cadre Employers
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

   btnRechercher = tk.Button(cadreEmployersEntry)
   btnRechercher['image'] = imgLoupe
   btnRechercher['relief'] = 'flat'
   btnRechercher['bg'] = '#ffffff'
   btnRechercher['fg'] = '#000000'
   btnRechercher['font'] = ('Calibri', '12', 'bold')
   btnRechercher['command'] = popupRecherche
   btnRechercher.grid(row=2, column=2)

   instructions()

   fenetre.mainloop()

def instructions():
   cadreInsturctions = tk.Frame(fenetre)
   cadreInsturctions['bg'] = arriereplan1
   cadreInsturctions.grid(row=0, column=0, rowspan=6, columnspan=4, sticky='nsew')

   lblInstructions = tk.Label(cadreInsturctions)
   lblInstructions['text'] = 'Instructions'
   lblInstructions['bg'] = arriereplan1
   lblInstructions['fg'] = '#000000'
   lblInstructions['font'] = ('Calibri', '12', 'bold')
   lblInstructions.grid(row=0, column=0, sticky='nsew')

   btnFermer = tk.Button(cadreInsturctions)
   btnFermer['text'] = 'Continuer'
   btnFermer['bg'] = '#ffffff'
   btnFermer['fg'] = '#000000'
   btnFermer['font'] = ('Calibri', '12', 'bold')
   btnFermer['command'] = cadreInsturctions.destroy
   btnFermer.grid(row=1, column=0)

   



# - Fonctions pour cadre
def update(x):
   global employes, rows, groupes, page_courant, employesTrouves, cadreRecherche, cadreResultat

   if x == "recherche": 
      for i in cadreResultat.winfo_children():
         if i != lblTxtNom and i != lblTxtPrenom and i != lblTxtPoste and i != lblTxtHeures and i != lblTxtSalaire: 
            i.destroy()
         else:
            pass

      for i, trouve in enumerate(employesTrouves):
         lblPersonne = tk.Label(cadreResultat)
         lblPersonne['text'] = trouve["nom"]
         lblPersonne['bg'] = '#ffffff'
         lblPersonne['fg'] = '#000000'
         lblPersonne['relief'] = 'groove'
         lblPersonne['width'] = 20
         lblPersonne['height'] = 2
         lblPersonne['font'] = ('Calibri', '12')
         lblPersonne.grid(row=i+1, column=0)

         lblPrenom = tk.Label(cadreResultat)
         lblPrenom['text'] = trouve["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Calibri', '12')
         lblPrenom.grid(row=i+1, column=1)

         lblPoste = tk.Label(cadreResultat)
         lblPoste['text'] = trouve["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Calibri', '12')
         lblPoste.grid(row=i+1, column=2)

         lblHeures = tk.Label(cadreResultat)
         lblHeures['text'] = trouve["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Calibri', '12')
         lblHeures.grid(row=i+1, column=3)

         lblSalaire = tk.Label(cadreResultat)
         lblSalaire['text'] = "$ {:.2f}".format(trouve["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Calibri', '12')
         lblSalaire.grid(row=i+1, column=4)
   else:
      for i in cadreEmployers.winfo_children():
         if i != lblTxttNom and i != lblTxttPrenom and i != lblTxttPoste and i != lblTxttHeures and i != lblTxttSalaire:
            i.destroy()
         else:
            pass
            
      updatePage()

      groupe_courant = groupes[page_courant-1]
      for i, employe in enumerate(groupe_courant):
         lblPersonne = tk.Label(cadreEmployers)
         lblPersonne['text'] = employe["nom"]
         lblPersonne['bg'] = '#ffffff'
         lblPersonne['fg'] = '#000000'
         lblPersonne['relief'] = 'groove'
         lblPersonne['width'] = 20
         lblPersonne['height'] = 2
         lblPersonne['font'] = ('Calibri', '12')
         lblPersonne.grid(row=i+1, column=0)

         lblPrenom = tk.Label(cadreEmployers)
         lblPrenom['text'] = employe["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Calibri', '12')
         lblPrenom.grid(row=i+1, column=1)

         lblPoste = tk.Label(cadreEmployers)
         lblPoste['text'] = employe["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Calibri', '12')
         lblPoste.grid(row=i+1, column=2)

         lblHeures = tk.Label(cadreEmployers)
         lblHeures['text'] = employe["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Calibri', '12')
         lblHeures.grid(row=i+1, column=3)

         lblSalaire = tk.Label(cadreEmployers)
         lblSalaire['text'] = "$ {:.2f}".format(employe["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Calibri', '12')
         lblSalaire.grid(row=i+1, column=4)

cadre()