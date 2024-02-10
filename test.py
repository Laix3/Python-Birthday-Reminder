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






objets = openFile('data.csv')

config = openFile('config.csv')

def add_to_csv(x,fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=x.keys())
        writer.writerow(x)

new_row = {'nom': 'Lebaeaeaec', 'prenom': 'Buyob', 'date': '31/02/2010'}
add_to_csv(new_row, 'test.csv')


# date = []
# for i in data:
#     date.append(i["date"])
# print(date)