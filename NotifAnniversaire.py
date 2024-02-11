import logging
import os
import winshell


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



def WStartup(src_file):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_name = f'{src_file}.lnk'
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    
    if os.path.exists(shortcut_path):
        print("L'option Windows Startup est activée, voulez-vous la désactiver ?")
        print('Y ou N')
        YorN = input("> ")

        if YorN.lower() == 'y':
            os.remove(shortcut_path)
            print("L'option Windows Startup est désormais désactivée.")
            logging.info("L'option Windows Startup est desormais désactivee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

    else:
        print("L'option Windows Startup est désactivée, voulez-vous l'activer ?")
        print('Y ou N')
        YorN = input("> ")

        if YorN.lower() == 'y':
            winshell.CreateShortcut(
                Path=os.path.join(startup_folder, f'{src_file}.lnk'),
                Target=src_file,
                Description="Script de démarrage pour la notification d'anniversaire"
            )
            print("L'option Windows Startup est désormais activée.")
            logging.info("L'option Windows Startup est desormais activee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")


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
            deletePeople()
            
        elif choice == '3':
            WStartup('NotifAnniversaire_startup.py')

                
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()