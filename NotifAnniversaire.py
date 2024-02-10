import csv
import os
import shutil
import sys
import logging

from NotifAnniversaire_startup import *


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)



def openFile(fichier):
    ''' Permet d'ouvrir un fichier csv et de convertir en dictionnaire
    in : exemple : file.csv
    out : dictionnaire du csv    
    '''
    try:
        file = open(fichier, 'r', encoding='utf8')

    except FileNotFoundError:
        logging.error('Fichier introuvable :/')
        print("Fichier introuvable :/")

    else:
        logging.info(f"Fichier, {fichier} ouvert")
        file = open(fichier, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=';')
        objets = [dict(ligne) for ligne in csv_en_dict]
    return objets


data = openFile('data.csv')
      
                
def add_to_csv(x,fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(x)
    print("Ajout effectué")
    logging.info(f"{x} écrit dans {fileName}")
    
    
def deletePeople():
    print


def main():
    print('''
Veuillez choisir une option parmi les suivantes :
    
    [1] Ajouter une personne
    [2] Supprimer une personne
    [3] ON/OFF Startup Windows
        
d3 : pour avoir la description de la commande [3]
''')
    
    while True:

        choice = input("> ")
        
        # if int(choice) == ValueError:
        #     print("Choix invalide. Veuillez sélectionner un chiffre.")
        
        if choice == 'd3':
            print("Permets que le script se lance au démargé de l'ordinateur pour vérifier si c'est l'anniversaire d'une personne")
            
        elif choice == '1':
            add = []
            
            nom = str(input("> Nom :"))
            add.append(nom)
            
            prenom = str(input("> Prenom :"))
            add.append(prenom)
            
            date = str(input("> Date :"))
            add.append(date)
            
            add_to_csv(add,'test.csv')
            add = []
            
        elif choice == '2':
            choice2 = input("> ")
            
        elif choice == '3':
            WStartup()

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()