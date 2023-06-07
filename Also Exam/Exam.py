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
entreesParPage = 8
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
   

def ajouter():
   global employes, postesoptions, rows, TEST

   try:
      lblErreur.destroy()
   except:
      pass
   if nom.get() and prenom.get() and heures.get():
      try:
         x = float(heures.get())
         if poste.get() == "Poste":
            erreur("Veuillez choisir un poste", "EmployersEntry")
         else:
            rows += 1
            employe = {
               "nom": nom.get(),
               "prenom": prenom.get(),
               "poste": poste.get(),
               "heures": heures.get(),
               "salaire": calcul_salaire(heures.get(), postesoptions.get(poste.get()))
            }
            employes.append(employe)
            grouper()
            if TEST == True:
               pass
            else:
               clear()
      except:
         erreur("Le nombre d'heures doit être un nombre", "EmployersEntry")
   else:
      erreur("Veuillez remplir tous les champs", "EmployersEntry")

def clear():
   entNom.delete(0, tk.END)
   entPrenom.delete(0, tk.END)
   entHeures.delete(0, tk.END)

def grouper():
   global entreesParPage, employes, groupes
   groupes.clear()
   nombreEmployes = len(employes)
   nombreGroupes = nombreEmployes // entreesParPage + (nombreEmployes % entreesParPage > 0)

   for i in range(nombreGroupes):
      debut = i * entreesParPage
      fin = (i+1) * entreesParPage
      groupe = employes[debut:fin]
      groupes.append(groupe)

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
      for i in employes:
         if recherche in i[typeSearch.lower()]:
            employesTrouves.append(i)
         else:
            erreur("Aucun résultat trouvé", "Recherche")
      if len(employesTrouves) == 0:
         erreur("Aucun résultat trouvé", "Recherche")
      else:
         update("recherche")
   else:
      erreur("Veuillez remplir tous les champs", "Recherche")

def popupRecherche():
   global typeRecherche, motcle, recherche, lblErreur, cadreRecherche, cadreResultat
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
   lblRecherche.grid(row=0, column=0)

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
   btnRechercher.grid(row=1, column=2)

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
fenetre.geometry("932x800")
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
cadreEmployers.grid(row=2, column=0, rowspan=3, columnspan=4, sticky='nsew')
cadreEmployers.grid_propagate(0)

cadreEmployersEntry = tk.Frame(fenetre)
cadreEmployersEntry['bg'] = '#ffffff'
cadreEmployersEntry['relief'] = 'groove'
cadreEmployersEntry['borderwidth'] = 2
cadreEmployersEntry.grid(row=1, column=0, rowspan=1, columnspan=4, sticky='nsew')

cadreOutils = tk.Frame(fenetre)
cadreOutils['bg'] = '#ffffff'
cadreOutils['relief'] = 'groove'
cadreOutils['borderwidth'] = 2
cadreOutils.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='nsew')
cadreOutils.grid_propagate(0)

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
btnAjouter.grid(row=2, column=0, columnspan=4)

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
lblTxtNom = tk.Label(cadreEmployers)
lblTxtNom['text'] = 'Nom'
lblTxtNom['bg'] = '#969696'
lblTxtNom['fg'] = '#000000'
lblTxtNom['width'] = 20
lblTxtNom['height'] = 2
lblTxtNom['borderwidth'] = 2
lblTxtNom['relief'] = 'groove'
lblTxtNom['font'] = ('Arial', '12')
lblTxtNom.grid(row=0, column=0)

lblTxtPrenom = tk.Label(cadreEmployers)
lblTxtPrenom['text'] = 'Prénom'
lblTxtPrenom['bg'] = '#969696'
lblTxtPrenom['fg'] = '#000000'
lblTxtPrenom['width'] = 20
lblTxtPrenom['height'] = 2
lblTxtPrenom['borderwidth'] = 2
lblTxtPrenom['relief'] = 'groove'
lblTxtPrenom['font'] = ('Arial', '12')
lblTxtPrenom.grid(row=0, column=1)

lblTxtPoste = tk.Label(cadreEmployers)
lblTxtPoste['text'] = 'Poste'
lblTxtPoste['bg'] = '#969696'
lblTxtPoste['fg'] = '#000000'
lblTxtPoste['width'] = 20
lblTxtPoste['height'] = 2
lblTxtPoste['borderwidth'] = 2
lblTxtPoste['relief'] = 'groove'
lblTxtPoste['font'] = ('Arial', '12')
lblTxtPoste.grid(row=0, column=2)

lblTxtHeures = tk.Label(cadreEmployers)
lblTxtHeures['text'] = 'Heures'
lblTxtHeures['bg'] = '#969696'
lblTxtHeures['fg'] = '#000000'
lblTxtHeures['width'] = 20
lblTxtHeures['height'] = 2
lblTxtHeures['borderwidth'] = 2
lblTxtHeures['relief'] = 'groove'
lblTxtHeures['font'] = ('Arial', '12')
lblTxtHeures.grid(row=0, column=3)

lblTxtSalaire = tk.Label(cadreEmployers)
lblTxtSalaire['text'] = 'Salaire'
lblTxtSalaire['bg'] = '#969696'
lblTxtSalaire['fg'] = '#000000'
lblTxtSalaire['width'] = 20
lblTxtSalaire['height'] = 2
lblTxtSalaire['borderwidth'] = 2
lblTxtSalaire['relief'] = 'groove'
lblTxtSalaire['font'] = ('Arial', '12')
lblTxtSalaire.grid(row=0, column=4)


# - Cadre Outils
lblOutils = tk.Label(cadreOutils)
lblOutils['text'] = 'Outils'
lblOutils['bg'] = '#ffffff'
lblOutils['fg'] = '#000000'
lblOutils['font'] = ('Arial', '20', 'bold')
lblOutils.grid(row=0, column=0)

btnRechercher = tk.Button(cadreOutils)
btnRechercher['image'] = imgLoupe
btnRechercher['relief'] = 'flat'
btnRechercher['bg'] = '#ffffff'
btnRechercher['fg'] = '#000000'
btnRechercher['font'] = ('Arial', '12', 'bold')
btnRechercher['command'] = popupRecherche
btnRechercher.grid(row=1, column=0)



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
         lblPersonne = tk.Label(cadreRecherche)
         lblPersonne['text'] = trouve["nom"]
         lblPersonne['bg'] = '#ffffff'
         lblPersonne['fg'] = '#000000'
         lblPersonne['relief'] = 'groove'
         lblPersonne['width'] = 20
         lblPersonne['height'] = 2
         lblPersonne['font'] = ('Arial', '12')
         lblPersonne.grid(row=i+4, column=0)

         lblPrenom = tk.Label(cadreRecherche)
         lblPrenom['text'] = trouve["prenom"]
         lblPrenom['bg'] = '#ffffff'
         lblPrenom['fg'] = '#000000'
         lblPrenom['relief'] = 'groove'
         lblPrenom['width'] = 20
         lblPrenom['height'] = 2
         lblPrenom['font'] = ('Arial', '12')
         lblPrenom.grid(row=i+4, column=1)

         lblPoste = tk.Label(cadreRecherche)
         lblPoste['text'] = trouve["poste"]
         lblPoste['bg'] = '#ffffff'
         lblPoste['fg'] = '#000000'
         lblPoste['relief'] = 'groove'
         lblPoste['width'] = 20
         lblPoste['height'] = 2
         lblPoste['font'] = ('Arial', '12')
         lblPoste.grid(row=i+4, column=2)

         lblHeures = tk.Label(cadreRecherche)
         lblHeures['text'] = trouve["heures"]
         lblHeures['bg'] = '#ffffff'
         lblHeures['fg'] = '#000000'
         lblHeures['relief'] = 'groove'
         lblHeures['width'] = 20
         lblHeures['height'] = 2
         lblHeures['font'] = ('Arial', '12')
         lblHeures.grid(row=i+4, column=3)

         lblSalaire = tk.Label(cadreRecherche)
         lblSalaire['text'] = "{:.2f} $".format(trouve["salaire"])
         lblSalaire['bg'] = '#ffffff'
         lblSalaire['fg'] = '#000000'
         lblSalaire['relief'] = 'groove'
         lblSalaire['width'] = 20
         lblSalaire['height'] = 2
         lblSalaire['font'] = ('Arial', '12')
         lblSalaire.grid(row=i+4, column=4)
   else:
      print("Erreur")
   for i in cadreEmployers.winfo_children():
      if i != lblTxtNom and i != lblTxtPrenom and i != lblTxtPoste and i != lblTxtHeures and i != lblTxtSalaire:
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