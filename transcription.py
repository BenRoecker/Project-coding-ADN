fichier = open("ADN_perfect.txt")
ARNmfichier = open("ARNm.txt","w")
lignes = fichier.readlines()
lignes = [line.rstrip('\n') for line in open("ADN.txt")]

def create_ARNm():
    liste = ""
    for base in lignes:
        base = base[0]
#on choisit de prendre que la première base de la paire
        if  base == "A":
            liste = liste + "U"
        elif base == "T":
            liste = liste + "A"
        elif base == "C":
            liste = liste + "G"
        elif base =="G":
            liste = liste + "C"
        else:
            liste = liste + "Error"
        liste = liste + "\n"
#On ajoute la base correpondantes et un retour à la ligne à la réponse
    return liste
#On retourne la réponse

ARNmfichier.write(create_ARNm())
fichier.close()
ARNmfichier.close()
