import csv
import os
import shutil
import sys

from CSV_by_Laix import *


objets = openFile('data.csv')
config = openFile('config.csv')


print(config)

# date = []
# for i in data:
#     date.append(i["date"])
# print(date)


# def WStartup():
#             config = openFile('config.csv')
            
#             WSvalue = []
#             for i in config:
#                 if i["name"] == 'startup':
#                     WSvalue.append(i["value"])

            
#             if int(WSvalue[0]) == 1 :
#                 print("L'option startup est activée, voulez-vous la désactiver ?")
#                 print('Y ou N')
#                 YorN = input("> ")
                
#                 if YorN.lower() == 'y':
#                     print('b') # remplacer le 0 par 1
#                 else:
#                     print('abb') 
                    
#             elif int(WSvalue[0]) == 0:
#                 print("L'option startup est désactivée, voulez-vous l'activer ?")
#                 print('Y ou N')
#                 YorN = input("> ")
                
#                 if YorN.lower() == 'y':
#                     print('a')
#                 else:
#                     print('abb')           
            
#             if int(WSvalue[0]) == 1 :
#                 startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
#                 dest_file = os.path.join(startup_folder, 'msg.py')
                
#                 if os.path.exists(dest_file):
#                     print("Démarrage automatique désactivé.")
#                     remove_Wstartup()
#                 else:
#                     print("Démarrage automatique activé.")
#                     add_Wstartup(sys.argv[0])
                    
#             else:
#                 print("nop")



# def add_Wstartup(src_file):
#     startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
#     dest_file = os.path.join(startup_folder, 'NotifAnniversaire.py')
#     if not os.path.exists(dest_file):
#         shutil.copy(src_file, dest_file)
#     else:
#         print("Le script est déjà dans les éléments de démarrage.")

# def remove_Wstartup():
#     startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
#     dest_file = os.path.join(startup_folder, 'NotifAnniversaire.py')
#     if os.path.exists(dest_file):
#         os.remove(dest_file)