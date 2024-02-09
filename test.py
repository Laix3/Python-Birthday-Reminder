import csv
import os
import shutil
import sys

def openFile(fichier):
    ''' Permet d'ouvrir un fichier csv et de convertir en dictionnaire
    in : example : file.csv
    out : dictionnaire du csv    
    '''
    try:
        file = open(fichier, 'r', encoding='utf8')

    except FileNotFoundError:
        print('Fichier introuvable :/')

    else:
        print('Fichier CSV trouvé !')
        file = open(fichier, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=';')
        objets = [dict(ligne) for ligne in csv_en_dict]
    return objets



def listCleanner(xList):
    ''' Permet d'enlever les '' d'un liste
    in : example : file.csv
    out : dictionnaire du csv    
    '''
    # verifie si c'est une liste
    if isinstance(xList, list):
        for i in xList:
            if i == '':
                xList.remove(i)
            else:
                pass
        print("Fin du nettoyage de la liste")

        return xList
    
    else:
        return "Cleaner : Vous n'avez pas sélectionné une liste"


objets = openFile('data.csv')

config = openFile('config.csv')

print(config)

# date = []
# for i in data:
#     date.append(i["date"])
# print(date)