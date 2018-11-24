#Programme altrenatif pour n'afficherque les molécules entre "met" et "Stop"

fichier = open("ARNm.txt")
PROTfichier = open("protéines.txt","w")
lignes = fichier.readlines()
lignes = [line.rstrip('\n') for line in open("ARNm.txt")]

def code_to_aa(code):
    if (code=="UUU" or code=="UUC"):
        return "Phe"
    elif (code=="UUA" or code=="UUG" or code=="CUU" or code=="CUC" or code=="CUA" or code=="CUG"):
        return "Leu"
    elif (code=="AUU" or code=="AUC" or code=="AUA"):
        return "Ile"
    elif (code=="AUG"):
        return "Met"
    elif (code=="GUU" or code=="GUC" or code=="GUA" or code=="GUG"):
        return "Val"
    elif (code=="UCU" or code=="UCC" or code=="UCA" or code=="UCG"):
        return "Ser"
    elif (code=="CCU" or code=="CCC" or code=="CCA" or code=="CCG"):
        return "Pro"
    elif (code=="ACU" or code=="ACC" or code=="ACA" or code=="ACG"):
        return "Thr"
    elif (code=="GCU" or code=="GCC" or code=="GCA" or code=="GCG"):
        return "Ala"
    elif (code=="UAU" or code=="UAC"):
        return "Tyr"
    elif (code=="UAA" or code=="UAG" or code=="UGA"):
        return "Stop"
    elif (code=="CAU" or code=="CAC"):
        return "His"
    elif (code=="CAA" or code=="CAG"):
        return "Gln"
    elif (code=="AAU" or code=="AAC"):
        return "Asn"
    elif (code=="AAA" or code=="AAG"):
        return "Lys"
    elif (code=="GAU" or code=="GAC"):
        return "Asp"
    elif (code=="GAA" or code=="GAG"):
        return "Glu"
    elif (code=="UGU" or code=="UGC"):
        return "Cys"
    elif (code=="UGG"):
        return "Trp"
    elif (code=="CGU" or code=="CGC" or code=="CGA" or code=="CGG"):
        return "Arg"
    elif (code=="AGU" or code=="AGC"):
        return "Ser"
    elif (code=="AGA" or code=="AGG"):
        return "Arg"
    elif (code=="GGU" or code=="GGC" or code=="GGA" or code=="GGG"):
        return "Gly"
    else:
        return "Error"
#Annexes

def create_PROT():
    code = ""
    ARN = ""
    for i in range(0,len(lignes)-3,3):
    #On cherche dans toute la liste
        code = lignes[i] + lignes[i+1] + lignes[i+2]
        #Création du paramètre
        if  code_to_aa(code) == "Met":
        #Lorsque l'on croise un codon start
            while not code_to_aa(code) == "Stop" and not i>len(lignes)-3:
            #et tant que l'on ne croise pas de codont Stop et que l'on dépasse pas le nombre d'élément dans la liste
                code = lignes[i] + lignes[i+1]+ lignes[i+2]
                #On crée encore le paramètre
                ARN = ARN + code_to_aa(code)
                #On ajoute le code de la protéine à la réponse
                i = i + 3
                #on augmente de 3 la variable d'itération
            ARN = ARN + "\n"
    return ARN
#returne la réponse lors de l'appel de la fonction
PROTfichier.write(create_PROT())
fichier.close()
PROTfichier.close()
