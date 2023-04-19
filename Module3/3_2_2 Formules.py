# ---------------------------------------------------------------------------------------------------------------------
# Nom : Joshua Nagy
# Titre : Exemlpe 3.2.2 Formules
# Description : Interface graphique présentant les résultats d'une formule mathématique
# ---------------------------------------------------------------------------------------------------------------------

# - Importaion des modules ------------------------------------------------------------------------------------------
import tkinter as tk

# - Programme principal ------------------------------------------------------------------------------------------

# - Déclaration des fonctions
def Calculer():
    x1 = int(X1.get())
    y1 = int(Y1.get())
    x2 = int(X2.get())
    y2 = int(Y2.get())
    pente = (y2-y1)/(x2-x1)
    lblResultat['text'] = "La pente est de: {}".format(pente)

# - Fenêtre  
fenetre = tk.Tk()
fenetre.title("Pente entre 2 points")
fenetre.geometry("400x300")
fenetre.configure(bg = "#ffffff")

# - Titre
lblTitre = tk.Label(fenetre)
lblTitre ['text'] = "Pente entre deux points"
lblTitre ['font'] = ["Arial", 20, "bold"]
lblTitre ['bg'] = "#ffffff"
lblTitre.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

# - Boite d'entrée point x1
lblX1 = tk.Label(fenetre)
lblX1 ['text'] = "X1"
lblX1 ['font'] = ["Arial", 15]
lblX1 ['bg'] = "#ffffff"
lblX1.grid(row = 1, column = 0, padx = 5, pady = 5)

X1 = tk.StringVar()
txtX1 = tk.Entry()
txtX1 ['width'] = 15
txtX1 ['font'] = ["Arial", 15]
txtX1 ['textvariable'] = X1
txtX1.grid(row = 1, column = 1, padx = 5, pady = 5)

# - Boite d'entrée point y1
lblY1 = tk.Label(fenetre)
lblY1 ['text'] = "Y1"
lblY1 ['font'] = ["Arial", 15]
lblY1 ['bg'] = "#ffffff"
lblY1.grid(row = 2, column = 0, padx = 5, pady = 5)

Y1 = tk.StringVar()
txtY1 = tk.Entry()
txtY1 ['width'] = 15
txtY1 ['font'] = ["Arial", 15]
txtY1 ['textvariable'] = Y1
txtY1.grid(row = 2, column = 1, padx = 5, pady = 5)

# - Boite d'entrée point x2
lblX2 = tk.Label(fenetre)
lblX2 ['text'] = "X2"
lblX2 ['font'] = ["Arial", 15]
lblX2 ['bg'] = "#ffffff"
lblX2.grid(row = 3, column = 0, padx = 5, pady = 5)

X2 = tk.StringVar()
txtX2 = tk.Entry()
txtX2 ['width'] = 15
txtX2 ['font'] = ["Arial", 15]
txtX2 ['textvariable'] = X2
txtX2.grid(row = 3, column = 1, padx = 5, pady = 5)

# - Boite d'entrée point y2
lblY2 = tk.Label(fenetre)
lblY2 ['text'] = "Y2"
lblY2 ['font'] = ["Arial", 15]
lblY2 ['bg'] = "#ffffff"
lblY2.grid(row = 4, column = 0, padx = 5, pady = 5)

Y2 = tk.StringVar()
txtY2 = tk.Entry()
txtY2 ['width'] = 15
txtY2 ['font'] = ["Arial", 15]
txtY2 ['textvariable'] = Y2
txtY2.grid(row = 4, column = 1, padx = 5, pady = 5)

# - Calculer
btnCalculer = tk.Button(fenetre)
btnCalculer ['text'] = "Calculer"
btnCalculer ['font'] = ["Arial", 15]
btnCalculer ['bg'] = "#ffffff"
btnCalculer ['command'] = Calculer
btnCalculer.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

# - Resultat
lblResultat = tk.Label(fenetre)
lblResultat ['text'] = "La pente est de: "
lblResultat ['font'] = ["Arial", 15]
lblResultat ['bg'] = "#ffffff"
lblResultat.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)


fenetre.mainloop()
