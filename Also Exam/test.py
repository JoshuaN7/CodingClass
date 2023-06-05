import tkinter as tk

# Variables
employes = []
postesoptions = {
    'Cuisinier': 19.00,
    'Serveur': 15.50,
    'Plongeur': 28.98,
    'Caissier': 15.98
}
impot_retenu = 0.105  # 10.5% de retenu sur le salaire

# Fonctions
def calcul_salaire(i):
    personne = employes[i]
    nb_heures = personne["heures"]
    taux_horaire = postesoptions.get(personne["poste"])
    salaire = nb_heures * taux_horaire
    impot = salaire * impot_retenu
    salaire_net = salaire - impot
    return salaire_net


def ajouter():
    nom = entNom.get()
    prenom = entPrenom.get()
    poste = dropPoste.get()
    heures = float(entHeures.get())

    if poste == "Poste":
        erreur("Veuillez choisir un poste")
    else:
        employe = {
            "nom": nom,
            "prenom": prenom,
            "poste": poste,
            "heures": heures,
            "salaires": calcul_salaire(len(employes))
        }
        employes.append(employe)

    update_employers()

def update_employers():
    # Clear previous employers
    for widget in cadreEmployers.winfo_children():
        widget.destroy()

    # Display employers
    lblTxtNom.grid(row=0, column=0)
    lblTxtPrenom.grid(row=0, column=1)
    lblTxtPoste.grid(row=0, column=2)
    lblTxtHeures.grid(row=0, column=3)
    lblTxtSalaire.grid(row=0, column=4)

    for i, employe in enumerate(employes, start=1):
        lblPersonne = tk.Label(cadreEmployers, text=employe["nom"])
        lblPersonne.grid(row=i, column=0)

        lblPrenom = tk.Label(cadreEmployers, text=employe["prenom"])
        lblPrenom.grid(row=i, column=1)

        lblPoste = tk.Label(cadreEmployers, text=employe["poste"])
        lblPoste.grid(row=i, column=2)

        lblHeures = tk.Label(cadreEmployers, text=employe["heures"])
        lblHeures.grid(row=i, column=3)

        lblSalaire = tk.Label(cadreEmployers, text=employe["salaires"])
        lblSalaire.grid(row=i, column=4)


def erreur(message):
    lblErreur.config(text=message)

# Fenetre
fenetre = tk.Tk()
fenetre.title("Comptabilité")

# Cadre EmployersEntry
cadreEmployersEntry = tk.Frame(fenetre)
cadreEmployersEntry.grid(row=1, column=0, sticky="nsew")


lblNom = tk.Label(cadreEmployersEntry, text='Nom')
lblNom.grid(row=0, column=0)

lblPrenom = tk.Label(cadreEmployersEntry, text='Prénom')
lblPrenom.grid(row=0, column=1)

lblPoste = tk.Label(cadreEmployersEntry, text='Poste')

# ...continued

# Initialize the available job positions
postesoptions = ["Manager", "Supervisor", "Employee"]
postesvar = tk.StringVar(fenetre)
postesvar.set(postesoptions[0])  # Set the default job position

lblPoste = tk.Label(fenetre, text="Poste:")
lblPoste.grid(row=0, column=0)

optPoste = tk.OptionMenu(fenetre, postesvar, *postesoptions)
optPoste.grid(row=0, column=1)

dropPoste = tk.OptionMenu(cadreEmployersEntry, postesvar, *postesoptions.keys())
dropPoste.grid(row=1, column=2)

lblHeures = tk.Label(cadreEmployersEntry, text='Heures')
lblHeures.grid(row=1, column=3)

entHeures = tk.Entry(cadreEmployersEntry)
entHeures.grid(row=1, column=4)

btnAjouter = tk.Button(cadreEmployersEntry, text="Ajouter", command=ajouter)
btnAjouter.grid(row=1, column=5)

# Cadre Employers
cadreEmployers = tk.Frame(fenetre)
cadreEmployers.grid(row=2, column=0, sticky="nsew")

lblTxtNom = tk.Label(cadreEmployers, text="Nom")
lblTxtPrenom = tk.Label(cadreEmployers, text="Prénom")
lblTxtPoste = tk.Label(cadreEmployers, text="Poste")
lblTxtHeures = tk.Label(cadreEmployers, text="Heures")
lblTxtSalaire = tk.Label(cadreEmployers, text="Salaire")

# Cadre Erreur
cadreErreur = tk.Frame(fenetre)
cadreErreur.grid(row=3, column=0, sticky="nsew")

lblErreur = tk.Label(cadreErreur, text="")
lblErreur.pack()

# Start the GUI main loop
fenetre.mainloop()

