import logging
import os
import shutil

from CSV_by_Laix import *


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


data = openFile('data.csv')

   
def deletePeople():
    print()
    # mettre ous biblio pandas car il y a la numerotation des ligne : https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python



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
        
        if choice.lower() == 'd3':
            print("Permets que le script se lance au démargé de l'ordinateur pour vérifier si c'est l'anniversaire d'une personne")
            
        elif choice == '1':
            NPD = []
            
            nom = str(input("> Nom : "))
            NPD.append(nom)
            
            prenom = str(input("> Prenom : "))
            NPD.append(prenom)
            
            date = str(input("> Date : "))
            NPD.append(date)
            
            add_csv(NPD,'data.csv')
            NPD = []
            
        elif choice == '2':
            choice2 = input("> ")
            
        elif choice == '3':

            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            dest_file = os.path.join(startup_folder, os.path.basename('NotifAnniversaire_startup.py'))
            
            if os.path.exists(dest_file) == True:
                print("L'option Windows Startup est activée, voulez-vous la désactiver ?")
                print('Y ou N')
                YorN = input("> ")

                if YorN.lower() == 'y':
                    os.remove(dest_file)

                    print("L'option Windows Startup est désormais désactivée")
                    logging.info("L'option Windows Startup est désormais désactivee")

                elif YorN.lower() == 'n':
                    pass

                else:
                    print("Choix invalide. Veuillez sélectionner une option valide.")
            
            else:
                print("L'option Windows Startup est désactivée, voulez-vous l'activer ?")
                print('Y ou N')
                YorN = input("> ")

                if YorN.lower() == 'y':
                    shutil.copy('NotifAnniversaire_startup.py', dest_file)

                    print("L'option Windows Startup est désormais activée")
                    logging.info("L'option Windows Startup est désormais activee")

                elif YorN.lower() == 'n':
                    pass

                else:
                    print("Choix invalide. Veuillez sélectionner une option valide.")

                
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()
