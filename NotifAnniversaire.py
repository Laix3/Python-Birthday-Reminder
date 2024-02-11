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
    # mettre ous biblio pandas car il y a la numerotation des ligne : https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
    
    

def WStartup(src_file):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    dest_file = os.path.join(startup_folder, os.path.basename(src_file))

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
            
            add_csv(NPD,'data.csv')
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
                    r = csv.reader(open('config.csv'))
                    lines = list(r)
                    lines[1][1] = 0
                    with open('test.csv', 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerows(lines)
                    
                else:
                    WStartup('NotifAnniversaire_startup.py')
                    
            elif WSvalue == 0:
                print("L'option startup est désactivée, voulez-vous l'activer ?")
                print('Y ou N')
                YorN = input("> ")
                
                if YorN.lower() == 'y':
                    WStartup('NotifAnniversaire_startup.py')
                else:
                    r = csv.reader(open('config.csv'))
                    lines = list(r)
                    lines[1][1] = 1
                    with open('test.csv', 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerows(lines)
                    
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()
