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

#importation des modules
import tkinter as tk

#programme principal

# - Variables
TEST = True
rows = 0
entreesParPage = 11
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
types = ["Nom", "Prenom", "Poste", "Heures", "Salaire"]
employesTrouves = []

# - Fonctions
def calcul_salaire(heures, taux_horaire):
   nb_heures = int(heures)
   salaire = nb_heures * taux_horaire
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
        if isinstance(recherche, float):
            for i in employes:
                if isinstance(i[typeSearch.lower()], float) and recherche == i[typeSearch.lower()]:
                    employesTrouves.append(i)
        else:
            for i in employes:
                if recherche.lower() in str(i[typeSearch.lower()]).lower():
                    employesTrouves.append(i)
        
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
   cadreRecherche.geometry("932x500")
   cadreRecherche['bg'] = '#ffffff'

   cadreResultat = tk.Frame(cadreRecherche)
   cadreResultat['bg'] = '#ffffff'
   cadreResultat['relief'] = "groove"
   cadreResultat['borderwidth'] = 2
   cadreResultat.grid(row = 3, column=0, columnspan=4, sticky='nsew')

   lblRecherche = tk.Label(cadreRecherche)
   lblRecherche['text'] = "Rechercher"
   lblRecherche['bg'] = '#ffffff'
   lblRecherche['fg'] = '#000000'
   lblRecherche['font'] = ('Arial', '12', 'bold')
   lblRecherche.grid(row=0, column=0, pady=5)

   lblType = tk.Label(cadreRecherche)
   lblType['text'] = "Type de recherche"
   lblType['bg'] = '#ffffff'
   lblType['fg'] = '#000000'
   lblType['font'] = ('Arial', '12', 'bold')
   lblType.grid(row=0, column=1)

   lblErreur = tk.Label(cadreRecherche)
   lblErreur['text'] = ""
   lblErreur['bg'] = '#ffffff'
   lblErreur['fg'] = '#ff0000'
   lblErreur['font'] = ('Arial', '12', 'bold')
   lblErreur.grid(row=0, column=3)

   motcle = tk.StringVar()
   entRecherche = tk.Entry(cadreRecherche)
   entRecherche['bg'] = '#ffffff'
   entRecherche['fg'] = '#000000'
   entRecherche['textvariable'] = motcle
   entRecherche['font'] = ('Arial', '12')
   entRecherche.grid(row=1, column=0)

   typeRecherche = tk.StringVar()
   typeRecherche.set("Nom")
   dropType = tk.OptionMenu(cadreRecherche, typeRecherche, *types)
   dropType['bg'] = '#ffffff'
   dropType['fg'] = '#000000'
   dropType['font'] = ('Arial', '12')
   dropType.grid(row=1, column=1)

   btnRechercher = tk.Button(cadreRecherche)
   btnRechercher['text'] = "Rechercher"
   btnRechercher['bg'] = '#ffffff'
   btnRechercher['fg'] = '#000000'
   btnRechercher['font'] = ('Arial', '12', 'bold')
   btnRechercher['command'] = search
   btnRechercher.grid(row=1, column=2, pady=20)

   lblTxtNom = tk.Label(cadreResultat)
   lblTxtNom['text'] = 'Nom'
   lblTxtNom['bg'] = '#969696'
   lblTxtNom['fg'] = '#000000'
   lblTxtNom['width'] = 20
   lblTxtNom['height'] = 2
   lblTxtNom['borderwidth'] = 2
   lblTxtNom['relief'] = 'groove'
   lblTxtNom['font'] = ('Arial', '12')
   lblTxtNom.grid(row=0, column=0)

   lblTxtPrenom = tk.Label(cadreResultat)
   lblTxtPrenom['text'] = 'Prénom'
   lblTxtPrenom['bg'] = '#969696'
   lblTxtPrenom['fg'] = '#000000'
   lblTxtPrenom['width'] = 20
   lblTxtPrenom['height'] = 2
   lblTxtPrenom['borderwidth'] = 2
   lblTxtPrenom['relief'] = 'groove'
   lblTxtPrenom['font'] = ('Arial', '12')
   lblTxtPrenom.grid(row=0, column=1)

   lblTxtPoste = tk.Label(cadreResultat)
   lblTxtPoste['text'] = 'Poste'
   lblTxtPoste['bg'] = '#969696'
   lblTxtPoste['fg'] = '#000000'
   lblTxtPoste['width'] = 20
   lblTxtPoste['height'] = 2
   lblTxtPoste['borderwidth'] = 2
   lblTxtPoste['relief'] = 'groove'
   lblTxtPoste['font'] = ('Arial', '12')
   lblTxtPoste.grid(row=0, column=2)

   lblTxtHeures = tk.Label(cadreResultat)
   lblTxtHeures['text'] = 'Heures'
   lblTxtHeures['bg'] = '#969696'
   lblTxtHeures['fg'] = '#000000'
   lblTxtHeures['width'] = 20
   lblTxtHeures['height'] = 2
   lblTxtHeures['borderwidth'] = 2
   lblTxtHeures['relief'] = 'groove'
   lblTxtHeures['font'] = ('Arial', '12')
   lblTxtHeures.grid(row=0, column=3)

   lblTxtSalaire = tk.Label(cadreResultat)
   lblTxtSalaire['text'] = 'Salaire'
   lblTxtSalaire['bg'] = '#969696'
   lblTxtSalaire['fg'] = '#000000'
   lblTxtSalaire['width'] = 20
   lblTxtSalaire['height'] = 2
   lblTxtSalaire['borderwidth'] = 2
   lblTxtSalaire['relief'] = 'groove'
   lblTxtSalaire['font'] = ('Arial', '12')
   lblTxtSalaire.grid(row=0, column=4)


def erreur(message, endroit):
   global lblErreur

   if endroit == "EmployersEntry":
      lblErreur = tk.Label(cadreEmployersEntry)
      lblErreur['text'] = message
      lblErreur['bg'] = '#ffffff'
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Arial', '12', 'bold')
      lblErreur.grid(row=3, column=0, columnspan=4, sticky='nsew')
   if endroit == "Recherche":
      lblErreur = tk.Label(cadreRecherche)
      lblErreur['text'] = message
      lblErreur['bg'] = '#ffffff'
      lblErreur['fg'] = '#ff0000'
      lblErreur['font'] = ('Arial', '12', 'bold')
      lblErreur.grid(row=2, column=0, columnspan=3, sticky='nsew')
   else:
      pass

# - Fenetre
fenetre = tk.Tk()
fenetre.title("Comptabilité")
fenetre.geometry("932x770")
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

# - images
imgFlecheGauche = tk.PhotoImage(file="flechegauche.gif")
imgFlecheDroite = tk.PhotoImage(file="flechedroite.gif")
imgLoupe = tk.PhotoImage(file="loupe.gif")

# - Cadres
cadreEmployers = tk.Frame(fenetre)
cadreEmployers['bg'] = '#ffffff'
cadreEmployers['relief'] = 'groove'
cadreEmployers['borderwidth'] = 2
cadreEmployers.grid(row=1, column=0, rowspan=4, columnspan=4, sticky='nsew')
cadreEmployers.grid_propagate(0)

cadreEmployersEntry = tk.Frame(fenetre)
cadreEmployersEntry['bg'] = '#ffffff'
cadreEmployersEntry['relief'] = 'groove'
cadreEmployersEntry['borderwidth'] = 2
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
lblNom['bg'] = '#ffffff'
lblNom['fg'] = '#000000'
lblNom['font'] = ('Arial', '12', 'bold')
lblNom.grid(row=0, column=0)

lblPrenom = tk.Label(cadreEmployersEntry)
lblPrenom['text'] = 'Prénom'
lblPrenom['bg'] = '#ffffff'
lblPrenom['fg'] = '#000000'
lblPrenom['font'] = ('Arial', '12', 'bold')
lblPrenom.grid(row=0, column=1)

lblPoste = tk.Label(cadreEmployersEntry)
lblPoste['text'] = 'Poste'
lblPoste['bg'] = '#ffffff'
lblPoste['fg'] = '#000000'
lblPoste['font'] = ('Arial', '12', 'bold')
lblPoste.grid(row=0, column=2)

lblHeures = tk.Label(cadreEmployersEntry)
lblHeures['text'] = 'Heures'
lblHeures['bg'] = '#ffffff'
lblHeures['fg'] = '#000000'
lblHeures['font'] = ('Arial', '12', 'bold')
lblHeures.grid(row=0, column=3)

nom = tk.StringVar()
entNom = tk.Entry(cadreEmployersEntry)
entNom['bg'] = '#ffffff'
entNom['fg'] = '#000000'
entNom['font'] = ('Arial', '12')
entNom['textvariable'] = nom
entNom.grid(row=1, column=0)

prenom = tk.StringVar()
entPrenom = tk.Entry(cadreEmployersEntry)
entPrenom['bg'] = '#ffffff'
entPrenom['fg'] = '#000000'
entPrenom['font'] = ('Arial', '12')
entPrenom['textvariable'] = prenom
entPrenom.grid(row=1, column=1)

poste = tk.StringVar()
poste.set("Poste")
dropPoste = tk.OptionMenu(cadreEmployersEntry, poste, *postesoptions)
dropPoste['bg'] = '#ffffff'
dropPoste['fg'] = '#000000'
dropPoste['font'] = ('Arial', '12')
dropPoste.grid(row=1, column=2)

heures = tk.StringVar()
entHeures = tk.Entry(cadreEmployersEntry)
entHeures['bg'] = '#ffffff'
entHeures['fg'] = '#000000'
entHeures['font'] = ('Arial', '12')
entHeures['textvariable'] = heures
entHeures.grid(row=1, column=3)

btnAjouter = tk.Button(cadreEmployersEntry)
btnAjouter['text'] = 'Ajouter'
btnAjouter['bg'] = '#ffffff'
btnAjouter['fg'] = '#000000'
btnAjouter['font'] = ('Arial', '12', 'bold')
btnAjouter['command'] = ajouter
btnAjouter.grid(row=2, column=1)

# - Porchain page
btnProchain = tk.Button(fenetre)
btnProchain['image'] = imgFlecheDroite
btnProchain['relief'] = 'flat'
btnProchain['bg'] = '#ffffff'
btnProchain['fg'] = '#000000'
btnProchain['font'] = ('Arial', '12', 'bold')
btnProchain['command'] = prochain
btnProchain.grid(row=5, column=3, sticky='e')

# - Page précédente
btnPrecedent = tk.Button(fenetre)
btnPrecedent['image'] = imgFlecheGauche
btnPrecedent['relief'] = 'flat'
btnPrecedent['bg'] = '#ffffff'
btnPrecedent['fg'] = '#000000'
btnPrecedent['font'] = ('Arial', '12', 'bold')
btnPrecedent['command'] = precedent
btnPrecedent.grid(row=5, column=0, sticky='w')

lblPage = tk.Label(fenetre)
lblPage['text'] = 'Page {} sur {}'.format(1,1)
lblPage['bg'] = '#ffffff'
lblPage['fg'] = '#000000'
lblPage['font'] = ('Arial', '12', 'bold')
lblPage.grid(row=5, column=1, columnspan=2)


# - Cadre Employers
lblTxttNom = tk.Label(cadreEmployers)
lblTxttNom['text'] = 'Nom'
lblTxttNom['bg'] = '#969696'
lblTxttNom['fg'] = '#000000'
lblTxttNom['width'] = 20
lblTxttNom['height'] = 2
lblTxttNom['borderwidth'] = 2
lblTxttNom['relief'] = 'groove'
lblTxttNom['font'] = ('Arial', '12')
lblTxttNom.grid(row=0, column=0)

lblTxttPrenom = tk.Label(cadreEmployers)
lblTxttPrenom['text'] = 'Prénom'
lblTxttPrenom['bg'] = '#969696'
lblTxttPrenom['fg'] = '#000000'
lblTxttPrenom['width'] = 20
lblTxttPrenom['height'] = 2
lblTxttPrenom['borderwidth'] = 2
lblTxttPrenom['relief'] = 'groove'
lblTxttPrenom['font'] = ('Arial', '12')
lblTxttPrenom.grid(row=0, column=1)

lblTxttPoste = tk.Label(cadreEmployers)
lblTxttPoste['text'] = 'Poste'
lblTxttPoste['bg'] = '#969696'
lblTxttPoste['fg'] = '#000000'
lblTxttPoste['width'] = 20
lblTxttPoste['height'] = 2
lblTxttPoste['borderwidth'] = 2
lblTxttPoste['relief'] = 'groove'
lblTxttPoste['font'] = ('Arial', '12')
lblTxttPoste.grid(row=0, column=2)

lblTxttHeures = tk.Label(cadreEmployers)
lblTxttHeures['text'] = 'Heures'
lblTxttHeures['bg'] = '#969696'
lblTxttHeures['fg'] = '#000000'
lblTxttHeures['width'] = 20
lblTxttHeures['height'] = 2
lblTxttHeures['borderwidth'] = 2
lblTxttHeures['relief'] = 'groove'
lblTxttHeures['font'] = ('Arial', '12')
lblTxttHeures.grid(row=0, column=3)

lblTxttSalaire = tk.Label(cadreEmployers)
lblTxttSalaire['text'] = 'Salaire'
lblTxttSalaire['bg'] = '#969696'
lblTxttSalaire['fg'] = '#000000'
lblTxttSalaire['width'] = 20
lblTxttSalaire['height'] = 2
lblTxttSalaire['borderwidth'] = 2
lblTxttSalaire['relief'] = 'groove'
lblTxttSalaire['font'] = ('Arial', '12')
lblTxttSalaire.grid(row=0, column=4)

btnRechercher = tk.Button(cadreEmployersEntry)
btnRechercher['image'] = imgLoupe
btnRechercher['relief'] = 'flat'
btnRechercher['bg'] = '#ffffff'
btnRechercher['fg'] = '#000000'
btnRechercher['font'] = ('Arial', '12', 'bold')
btnRechercher['command'] = popupRecherche
btnRechercher.grid(row=2, column=2)



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
         lblPersonne['font'] = ('Arial', '12')
         lblPersonne.grid(row=i+1, column=0)

         lblPrenom = tk.Label(cadreResultat)
         lblPrenom['text'] = trouve["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Arial', '12')
         lblPrenom.grid(row=i+1, column=1)

         lblPoste = tk.Label(cadreResultat)
         lblPoste['text'] = trouve["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Arial', '12')
         lblPoste.grid(row=i+1, column=2)

         lblHeures = tk.Label(cadreResultat)
         lblHeures['text'] = trouve["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Arial', '12')
         lblHeures.grid(row=i+1, column=3)

         lblSalaire = tk.Label(cadreResultat)
         lblSalaire['text'] = "{:.2f} $".format(trouve["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Arial', '12')
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
         lblPersonne['font'] = ('Arial', '12')
         lblPersonne.grid(row=i+1, column=0)

         lblPrenom = tk.Label(cadreEmployers)
         lblPrenom['text'] = employe["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Arial', '12')
         lblPrenom.grid(row=i+1, column=1)

         lblPoste = tk.Label(cadreEmployers)
         lblPoste['text'] = employe["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Arial', '12')
         lblPoste.grid(row=i+1, column=2)

         lblHeures = tk.Label(cadreEmployers)
         lblHeures['text'] = employe["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Arial', '12')
         lblHeures.grid(row=i+1, column=3)

         lblSalaire = tk.Label(cadreEmployers)
         lblSalaire['text'] = "{:.2f} $".format(employe["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Arial', '12')
         lblSalaire.grid(row=i+1, column=4)

fenetre.mainloop()