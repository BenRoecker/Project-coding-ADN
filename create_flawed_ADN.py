fichier = open("ADN.txt", "w")
import random
listbases = ["A=T","T=A","C=G","G=C"]
base = ["A","T","C","G"]
#Création d'une liste contenant les bases seules

def create_flawed_adn():
    listebase = ""
    for i in range(1,1001):
#On souhaite obtenir 1000 paires de bases
        erreur = random.randint(1,20)
#Création d'une erreur aléatoire
        if erreur == 1:
            base1 = random.choice(base)
            base2 = random.choice(base)
            pairebase = base1 + "=" + base2
#Appariement de 2 bases aléatoires permettant les erreurs
        else:
            pairebase = random.choice(listbases)
#Création d'une paires de base correct
        listebase = listebase + pairebase + "\n"
#ajout de la paire de base crée à la réponse
    return listebase

fichier.write(create_flawed_adn())
fichier.close()
