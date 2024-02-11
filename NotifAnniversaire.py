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
    print()
    
    

def WStartup(src_file):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    # Chemin de destination du fichier dans le dossier de démarrage
    dest_file = os.path.join(startup_folder, os.path.basename(src_file))

    # Copie le fichier source dans le dossier de démarrage
    shutil.copy(src_file, dest_file)

    print("Le programme a ete ajoute au demarrage de Windows.")
    logging.info("Le programme a ete ajoute au demarrage de Windows.")


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
            config = openFile('config.csv')
            
            WSvalue = None
            
            for i in config:
                if i["name"] == 'startup':
                    WSvalue = i["value"]

            
            if WSvalue == 1 :
                print("L'option startup est activée, voulez-vous la désactiver ?")
                print('Y ou N')
                YorN = input("> ")
                
                if YorN.lower() == 'y':
                    print('b') # remplacer le 0 par 1
                else:
                    print('abb') 
                    
            elif WSvalue == 0:
                print("L'option startup est désactivée, voulez-vous l'activer ?")
                print('Y ou N')
                YorN = input("> ")
                
                if YorN.lower() == 'y':
                    print('a')
                else:
                    print('abb')           
                    
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()
