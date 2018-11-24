fichier = open("ADN.txt","r")
lignes = fichier.readlines()
#Lis le contenu du fichier et palce chaque ligne dans une liste
lignes = [line.rstrip('\n') for line in open("ADN.txt")]
fichier.close()
fichier = open("ADN.txt","a")
#Pour supprimer le retour à la ligne de chaque élément de la liste
listbases = ["A=T","T=A","C=G","G=C"]
def count_ADN():
    nombrerreur = 0
#Initialisation de la réponse
    for base in lignes:
        if not base in listbases:
#Si l'élément de la liste n'est pas une base
            nombrerreur += 1
    return nombrerreur
#On ajoute 1 au nombre d'erreur
fichier.write("Il y a "+count_ADN()+" erreurs.")
fichier.close()
