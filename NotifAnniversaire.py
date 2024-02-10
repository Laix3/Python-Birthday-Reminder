import csv
import os
import shutil
import sys
import logging


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


def add_to_startup_windows(src_file):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    dest_file = os.path.join(startup_folder, 'NotifAnniversaire.py')
    if not os.path.exists(dest_file):
        shutil.copy(src_file, dest_file)
    else:
        print("Le script est déjà dans les éléments de démarrage.")

def remove_from_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    dest_file = os.path.join(startup_folder, 'NotifAnniversaire.py')
    if os.path.exists(dest_file):
        os.remove(dest_file)



def WStartup():
            config = openFile('config.csv')
            
            WSvalue = []
            for i in config:
                if i["name"] == 'startup':
                    WSvalue.append(i["value"])

            
            if int(WSvalue[0]) == 1 :
                print("L'option startup est activée, voulez-vous la désactiver ?")
                print('Y ou N')
                YorN = input("> ")
                
                if YorN.lower() == 'y':
                    print('b') # remplacer le 0 par 1
                else:
                    print('abb') 
                    
            elif int(WSvalue[0]) == 0:
                print("L'option startup est désactivée, voulez-vous l'activer ?")
                print('Y ou N')
                YorN = input("> ")
                
                if YorN.lower() == 'y':
                    print('a')
                else:
                    print('abb')           
            
            if int(WSvalue[0]) == 1 :
                startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
                dest_file = os.path.join(startup_folder, 'NotifAnniversaire.py')
                
                if os.path.exists(dest_file):
                    print("Démarrage automatique désactivé.")
                    remove_from_startup_windows()
                else:
                    print("Démarrage automatique activé.")
                    add_to_startup_windows(sys.argv[0])
                    
            else:
                print("nop")
                
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
    [4] Ouvrir la liste
        
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