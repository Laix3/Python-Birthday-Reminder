import csv
import os
import shutil
import sys

from CSV_by_Laix import *


data = openFile('data.csv')
config = openFile('config.csv')

x = data.lower()
print(x)

def remove_person():
    print("Vous pouvez supprimer une personne directement dans le fichier data.csv (il faut une ligne vide à la fin)")
    print("Veuillez entrer les informations de la personne que vous souhaitez supprimer")
    nom = input("> Nom : ")


    recherche1 = []
    for i in data:
        if i["nom"] == nom:
            recherche1.append(i)

    if len(recherche1) > 1:
        prenom = input("> Prenom : ")
        recherche2 = []
        for i in recherche1:
            if i["prenom"] == prenom:
                recherche2.append(i)
        return recherche2
    else:
        print("Une erreur est survenue lors de la recherche pour suppression")
    
    return recherche1

print(remove_person())