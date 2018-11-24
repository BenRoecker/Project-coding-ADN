from tkinter import *
import random
#importation des bibliothèque nécessaires
from create_ADN import *
from create_flawed_ADN import *
#Importation des autres programmes

fenetre = Tk()
#permet d'ouvrir une fenetre graphique
fenetre.title("ADN")



def creationadn():
    Bases.delete("1.0",END)
    #efface tout le text présent
    Bases.insert(END,create_adn())
    #Ajoute à la fin(END) les 1000 bases de create_adn()

#Fonction qui affiche 1000 bases sans erreurs

def creationfauxadn():
    Bases.delete("1.0",END)
    Bases.insert(END,create_flawed_adn())
#Fonctions qui affiche 1000 bases avec des erreurs

menubar = Menu(fenetre)
menu1 = Menu(menubar,tearoff = 0)
menu1.add_command(label="créer l'ADN",command=creationadn)
menu1.add_command(label="Créer l'ADN avec des erreurs",command=creationfauxadn)
menu1.add_separator()
menu1.add_command(label="Quitter",command=fenetre.destroy)
menubar.add_cascade(label="Création", menu=menu1)
#permet de créer un menu déroulant
fenetre.config(menu=menubar)
#Affiche ce menu déroulant
case = Canvas(fenetre, width=600, height=400)
#Créer un case pour y mettre des objets
case.grid(row=0, column=0)
#affiche et positionne la case
Bases = Text(fenetre, height=50, width=100)
#créer une zone de texte
Bases.grid(row=0,column=0)
Bases.insert(END,"ADN")
scroll = Scrollbar(fenetre, orient='vertical',command=Bases.yview)
scroll.grid(row=0, column=1, sticky='ns')


fichier.close()
#ferme le fichier
