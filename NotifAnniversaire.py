import platform
import os

from CSV_by_Laix import *


print("[*] Installing missing modules")

if platform.system().startswith("Windows"):
    try:
        import csv
    except ImportError:
        os.system("python -m pip install csv -q -q -q")
        import csv

    try:
        import ctypes
    except ImportError:
        os.system("python -m pip install ctypes -q -q -q")
        import ctypes

    try:
        import datetime
    except ImportError:
        os.system("python -m pip install datetime -q -q -q")
        import datetime

    try:
        import winshell
    except ImportError:
        os.system("python -m pip install winshell -q -q -q")
        os.system("python -m pip install pywin32 -q -q -q")
        import winshell

    try:
        import logging
    except ImportError:
        os.system("python -m pip install logging -q -q -q")
        import logging

    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Linux"):
    print("[*] La version Linux n'est pas encore disponible. Vous devez lancer le programme sur Windows ou MacOS.")

elif platform.system().startswith("Darwin"):
    print("[*] La version MacOS n'est pas encore disponible. Vous devez lancer le programme sur Windows ou MacOS.")




logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


data = openFile('data.csv')


def remove_person():
    print("Vous pouvez supprimer une personne directement dans le fichier data.csv (il faut une ligne vide à la fin)")
    print("[*] Veuillez entrer les informations de la personne que vous souhaitez supprimer")
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

        print(f"[*] Suppression de {recherche1} réussie avec succès")
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

        print(f"[*] Suppression de {recherche2} réussie avec succès")
        logging.info(f"Suppression de {recherche2} reussie avec succes")



def WStartup(src_file):
    # C:\Users\Laix\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_name = f'{src_file}.lnk'
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    
    if os.path.exists(shortcut_path):
        print("[*] L'option Windows Startup est activée, voulez-vous la désactiver ?")
        print('Y ou N')
        YorN = input("> ")

        if YorN.lower() == 'y':
            os.remove(shortcut_path)
            print("[*] L'option Windows Startup est désormais désactivée.")
            logging.info("L'option Windows Startup est desormais désactivee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

    else:
        print("[*] L'option Windows Startup est désactivée, voulez-vous l'activer ?")
        print('Y ou N')
        YorN = input("> ")

        if YorN.lower() == 'y':
            winshell.CreateShortcut(
                Path=os.path.join(startup_folder, f'{src_file}.lnk'),
                Target=src_file,
                Description="Script de démarrage pour la notification d'anniversaire"
            )
            print("[*] L'option Windows Startup est désormais activée.")
            logging.info("L'option Windows Startup est desormais activee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("[*] Choix invalide. Veuillez sélectionner une option valide.")



def main():
    print('''
Veuillez choisir une option parmi les suivantes :
    
    [1] Ajouter une personne
    [2] Supprimer une personne
    [3] ON/OFF Startup Windows
    [4] Any problems with startup ?
        
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
            
            add_to_csv(NPD,'data.csv')
            NPD = []
            
        elif choice == '2':
            remove_person()
            
        elif choice == '3':
            WStartup('NotifAnniversaire_startup.py')
                
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
        
main()