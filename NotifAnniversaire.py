import logging

from NotifAnniversaire_startup import *
from CSV_by_Laix import *


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


data = openFile('data.csv')
      
   
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
            NPD = []
            
            nom = str(input("> Nom : "))
            NPD.append(nom)
            
            prenom = str(input("> Prenom : "))
            NPD.append(prenom)
            
            date = str(input("> Date : "))
            NPD.append(date)
            
            add_to_csv(NPD,'data.csv')
            NPD = []
            
        elif choice == '2':
            choice2 = input("> ")
            
        elif choice == '3':
            WStartup()

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()