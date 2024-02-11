import csv
import os
import shutil
import sys

from CSV_by_Laix import *


data = openFile('data.csv')
config = openFile('config.csv')


def remove_person():
    print("Vous pouvez supprimer une personne directement dans le fichier data.csv (il faut une ligne vide à la fin)")
    print("Veuillez entrer les informations de la personne que vous souhaitez supprimer")
    nom = input("> Nom : ")

    recherche1 = []
    for i in data:
        if i["nom"] == nom.lower():
            recherche1.append(i)
    
    if len(recherche1) <= 1:
        data_restant = [personne for personne in data if personne not in recherche1]

        with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nom', 'prenom', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(data_restant)

        print(f"Suppression de {recherche1} réussie avec succès")
        logging.info(f"Suppression de {recherche1} reussie avec succes")


    elif len(recherche1) > 1:
        prenom = input("> Prenom : ")

        recherche2 = []
        for i in recherche1:
            if i["prenom"] == prenom.lower():
                recherche2.append(i)

        data_restant = [personne for personne in data if personne not in recherche2]

        with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nom', 'prenom', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(data_restant)

        print(f"Suppression de {recherche2} réussie avec succès")
        logging.info(f"Suppression de {recherche2} reussie avec succes")

remove_person()