#Crée de l'ADN parfait

fichier = open("ADN.txt", "w")
#Ouvrir un fichier , écraser à chaque fois son contenu
import random
#Apporte l'aléatoire dans ce programme
listbases = ["A=T","T=A","C=G","G=C"]
#Crée une liste contenant toutes les bases

def create_adn():#Fonction de création
    listebase = ""
#Initialisation de la réponse
    for i in range(1,1001):
#On veut obtenir 1000 bases
        base =random.choice(listbases)
#On choisi une base aléatoire dans la liste les contenant toutes
        listebase = listebase +  base + "\n"
#Ajout de la base et d'un retour à la ligne à la réponse
    return listebase
#L'appel de la fonction returne la réponse

fichier.write(create_adn())
#Ecrire la réponse dans le fichier
fichier.close()
#Fermer le fichier
