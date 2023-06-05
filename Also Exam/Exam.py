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
import math

#programme principal

# - Variables
TEST = True
rows = 0
page_courant = 1
entries_par_page = 8
employes = []
postesoptions = {
   'Cuisinier' : 19.00,
   'Serveur' : 15.50,
   'Plongeur' : 28.98,
   'Caissier' : 15.98
}

impot_retenu = 0.105  #10,5% de retenu sur le salaire

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
            erreur("Veuillez choisir un poste")
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
            update()
            if TEST == True:
               pass
            else:
               clear()
      except:
         erreur("Le nombre d'heures doit être un nombre")
   else:
      erreur("Veuillez remplir tous les champs")

def clear():
   entNom.delete(0, tk.END)
   entPrenom.delete(0, tk.END)
   entHeures.delete(0, tk.END)

def prochain():
   global page_courant
   page_courant += 1

def precedent():
   global page_courant
   page_courant -= 1
   print("precedent")

def erreur(message):
   global lblErreur
   lblErreur = tk.Label(cadreEmployersEntry)
   lblErreur['text'] = message
   lblErreur['bg'] = '#ffffff'
   lblErreur['fg'] = '#ff0000'
   lblErreur['font'] = ('Arial', '12', 'bold')
   lblErreur.grid(row=3, column=0, columnspan=4, sticky='nsew')

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
btnProchain['bg'] = '#ffffff'
btnProchain['fg'] = '#000000'
btnProchain['font'] = ('Arial', '12', 'bold')
btnProchain['command'] = prochain
btnProchain.grid(row=5, column=3, sticky='e')

# - Page précédente
btnPrecedent = tk.Button(fenetre)
btnPrecedent['image'] = imgFlecheGauche
btnPrecedent['bg'] = '#ffffff'
btnPrecedent['fg'] = '#000000'
btnPrecedent['font'] = ('Arial', '12', 'bold')
btnPrecedent['command'] = precedent
btnPrecedent.grid(row=5, column=0, sticky='w')

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


# - Fonctions pour cadre
def update():
   global employes, rows
   for i in range(rows):
      lblPersonne = tk.Label(cadreEmployers)
      lblPersonne['text'] = employes[i]["nom"]
      lblPersonne['bg'] = '#ffffff'
      lblPersonne['fg'] = '#000000'
      lblPersonne['relief'] = 'groove'
      lblPersonne['width'] = 20
      lblPersonne['height'] = 2
      lblPersonne['font'] = ('Arial', '12')
      lblPersonne.grid(row=i+1, column=0)

   for i in range(rows):
      lblPrenom = tk.Label(cadreEmployers)
      lblPrenom['text'] = employes[i]["prenom"]
      lblPrenom['bg'] = '#ffffff'
      lblPrenom['fg'] = '#000000'
      lblPrenom['relief'] = 'groove'
      lblPrenom['width'] = 20
      lblPrenom['height'] = 2
      lblPrenom['font'] = ('Arial', '12')
      lblPrenom.grid(row=i+1, column=1)

   for i in range(rows):
      lblPoste = tk.Label(cadreEmployers)
      lblPoste['text'] = employes[i]["poste"]
      lblPoste['bg'] = '#ffffff'
      lblPoste['fg'] = '#000000'
      lblPoste['relief'] = 'groove'
      lblPoste['width'] = 20
      lblPoste['height'] = 2
      lblPoste['font'] = ('Arial', '12')
      lblPoste.grid(row=i+1, column=2)

   for i in range(rows):
      lblHeures = tk.Label(cadreEmployers)
      lblHeures['text'] = employes[i]["heures"]
      lblHeures['bg'] = '#ffffff'
      lblHeures['fg'] = '#000000'
      lblHeures['relief'] = 'groove'
      lblHeures['width'] = 20
      lblHeures['height'] = 2
      lblHeures['font'] = ('Arial', '12')
      lblHeures.grid(row=i+1, column=3)

   for i in range(rows):
      lblSalaire = tk.Label(cadreEmployers)
      lblSalaire['text'] = "{:.2f} $".format(employes[i]["salaire"])
      lblSalaire['bg'] = '#ffffff'
      lblSalaire['fg'] = '#000000'
      lblSalaire['relief'] = 'groove'
      lblSalaire['width'] = 20
      lblSalaire['height'] = 2
      lblSalaire['font'] = ('Arial', '12')
      lblSalaire.grid(row=i+1, column=4)


fenetre.mainloop()
