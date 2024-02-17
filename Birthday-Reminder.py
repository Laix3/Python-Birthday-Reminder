import os

from CSV_by_Laix import *


print("\033[91m" + "[*] Installing missing modules..." + "\033[97m") 


try:
    import platform
except ImportError:
    os.system("py -m pip install platform -q -q -q")
import platform
    
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
    
try:
    import plyer
except ImportError:
    os.system("py -m pip install plyer -q -q -q")
    
    


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


data = openFile('data.csv')


def remove_person():
    print("\033[92m" + "[+] Please enter the information of the person you want to remove" + "\033[97m")
    nom = input("> Name : ")

    recherche1 = []
    for i in data:
        if i["name"] == nom.lower():
            recherche1.append(i)
    
    if len(recherche1) <= 1:
        data_restant = [personne for personne in data if personne not in recherche1]

        with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'fname', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(data_restant)

        print("\033[93m" + f"[-] Successfully removed {recherche1}" + "\033[97m")
        logging.info(f"Successfully removed {recherche1}")


    elif len(recherche1) > 1:
        prenom = input("> First Name : ")

        recherche2 = []
        for i in recherche1:
            if i["fname"] == prenom.lower():
                recherche2.append(i)

        data_restant = [personne for personne in data if personne not in recherche2]

        with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'fname', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(data_restant)

        print(f"[-] Successfully removed {recherche2}")
        logging.info(f"Successfully removed {recherche2}")



def WStartup(src_file):

    if platform.system().startswith("Windows"):

        startup_folder = winshell.startup()
        shortcut_path = os.path.join(startup_folder, f'{src_file}.lnk')
        script_directory = os.path.dirname(os.path.abspath(__file__))


        if os.path.exists(shortcut_path):
            print("[*] Windows Startup option is \033[92menabled\033[97m, do you want to \033[91mdisable\033[97m it ?")
            print('\033[91mY\033[97m or \033[92mN\033[97m')
            YorN = input("> ")

            if YorN.lower() == 'y':
                os.remove(shortcut_path)
                print("[*] Windows Startup option is now \033[91mdisabled.\033[97m")
                logging.info("Windows Startup option is now disabled.")

            elif YorN.lower() == 'n':
                pass

            else:
                print("\033[91m" + "Invalid choice. Please select a valid option." + "\033[97m")

        else:
            print("[*] Windows Startup option is \033[91mdisabled\033[97m, do you want to \033[92menable\033[97m it ?")
            print('\033[92mY\033[97m or \033[91mN\033[97m')
            YorN = input("> ")

            if YorN.lower() == 'y':
                
                winshell.CreateShortcut(
                    Path=shortcut_path, 
                    Target=os.path.abspath(src_file),
                    StartIn=script_directory,
                    Description="Script for birthday notification at startup")
                

                print("[*] Windows Startup option is now \033[92menabled.\033[97m")
                logging.info("Windows Startup option is now enabled.")

            elif YorN.lower() == 'n':
                pass

            else:
                print("\033[91m" + "Invalid choice. Please select a valid option." + "\033[97m")
    
    elif platform.system().startswith("Linux"):
        print("not avaible on linux")

    elif platform.system().startswith("Darwin"):
        print("not avaible on MacOs")
    
    else:
        raise OSError("\033[91mUnsupported operating system: " + platform.system() + "\033[97m")


def main():
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple, Box.DoubleCube('''
Please choose an option from the following:

[1] Add a person
[2] Delete a person
[3] ON/OFF Windows Startup
        
d3: for the description of command [3]
''')))
    
    while True:

        choice = input("> ")
        
        if choice.lower() == 'd3':
            print("Allows the script to run on computer startup to check if it's someone's birthday")
            
        elif choice == '1':
            NPD = []
            
            nom = str(input("> Name : "))
            NPD.append(nom)
            
            prenom = str(input("> First Name : "))
            NPD.append(prenom)
            
            date = str(input("> Birthday : "))
            NPD.append(date)
            
            add_to_csv(NPD,'data.csv')
            NPD = []
            
        elif choice == '2':
            remove_person()
            
        elif choice == '3':
            WStartup('Birthday-Reminder_startup.pyw')
                
        else:
            print("\033[91m" + "[*] Invalid choice. Please select a valid option." + "\033[97m")
        
main()