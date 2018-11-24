fichier = open("ADN.txt")
perfectfichier = open("ADN_perfect.txt","w")
lignes = fichier.readlines()
lignes = [line.rstrip('\n') for line in open("ADN.txt")]

listbases = ["A=T","T=A","C=G","G=C"]

def create_repair_ADN():
    liste = ""
    for base in lignes:
    #pour chaque base dans la liste
        if  base in listbases:
        #si la base est dans la liste préconsu
            liste = liste + base + "\n"
            #alors on l'ajoute à la répones
    return liste
perfectfichier.write(create_repair_ADN())
fichier.close()
perfectfichier.close()
