import os
import platform
from pystyle import *

from CSV_by_Laix import *

print("\033[91m" + "[*] Installing missing modules" + "\033[97m") 

if platform.system().startswith("Windows"):
    try:
        import csv
    except ImportError:
        os.system("py -m pip install csv -q -q -q")
        import csv

    try:
        import ctypes
    except ImportError:
        os.system("py -m pip install ctypes -q -q -q")
        import ctypes

    try:
        import datetime
    except ImportError:
        os.system("py -m pip install datetime -q -q -q")
        import datetime

    try:
        import winshell
    except ImportError:
        os.system("py -m pip install winshell -q -q -q")
        os.system("py -m pip install pywin32 -q -q -q")
        import winshell

    try:
        import logging
    except ImportError:
        os.system("py -m pip install logging -q -q -q")
        import logging

    try:
        import colorama
    except ImportError:
        os.system("py -m pip install colorama -q -q -q")
        from colorama import Fore, Back, Style

    try:
        import pystyle
    except ImportError:
        os.system("py -m pip install pystyle -q -q -q")
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
    print("\033[92m" + "[*] Veuillez entrer les informations de la personne que vous souhaitez supprimer" + "\033[97m")
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

        print("\033[93m" + f"[*] Suppression de {recherche1} réussie avec succès" + "\033[97m")
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
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, f'{src_file}.lnk')
    script_directory = os.path.dirname(os.path.abspath(__file__))


    if os.path.exists(shortcut_path):
        print("[*] L'option Windows Startup est \033[92mactivée\033[97m, voulez-vous la \033[91mdésactiver\033[97m ?")
        print('\033[91mY\033[97m or \033[92mN\033[97m')
        YorN = input("> ")

        if YorN.lower() == 'y':
            os.remove(shortcut_path)
            print("[*] L'option Windows Startup est désormais \033[91mdésactivée.\033[97m")
            logging.info("L'option Windows Startup est desormais désactivee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("\033[91m" + "Choix invalide. Veuillez sélectionner une option valide." + "\033[97m")

    else:
        print("[*] L'option Windows Startup est \033[91mdésactivée\033[97m, voulez-vous \033[92ml'activer\033[97m ?")
        print('\033[92mY\033[97m or \033[91mN\033[97m')
        YorN = input("> ")

        if YorN.lower() == 'y':
            
            winshell.CreateShortcut(
                Path=shortcut_path, 
                Target=os.path.abspath(src_file),
                StartIn=script_directory,
                Description="Script de démarrage pour les notifications d'anniversaire")
            

            print("[*] L'option Windows Startup est désormais \033[92mactivée.\033[97m")
            logging.info("L'option Windows Startup est desormais activee.")

        elif YorN.lower() == 'n':
            pass

        else:
            print("\033[91m" + "[*] Choix invalide. Veuillez sélectionner une option valide." + "\033[97m")



def main():
    print(Colorate.Horizontal(Colors.blue_to_purple, Box.DoubleCube('''
Veuillez choisir une option parmi les suivantes :
    
[1] Ajouter une personne
[2] Supprimer une personne
[3] ON/OFF Startup Windows
        
d3 : pour avoir la description de la commande [3]
''')))
    
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
            
            date = str(input("> Anniversaire : "))
            NPD.append(date)
            
            add_to_csv(NPD,'data.csv')
            NPD = []
            
        elif choice == '2':
            remove_person()
            
        elif choice == '3':
            WStartup('NotifAnniversaire_startup.py')
                
        else:
            print("\033[91m" + "[*] Choix invalide. Veuillez sélectionner une option valide." + "\033[97m")
        
main()