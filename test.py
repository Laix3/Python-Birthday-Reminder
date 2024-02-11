import csv
import os
import shutil
import sys

def openFile(fichier):
    ''' Permet d'ouvrir un fichier csv et de convertir en dictionnaire
    in : example : file.csv
    out : dictionnaire du csv    
    '''
    try:
        file = open(fichier, 'r', encoding='utf8')

    except FileNotFoundError:
        print('Fichier introuvable :/')

    else:
        print('Fichier CSV trouvé !')
        file = open(fichier, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=';')
        objets = [dict(ligne) for ligne in csv_en_dict]
    return objets






objets = openFile('data.csv')

config = openFile('config.csv')

def add_to_csv(x,fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=x.keys())
        writer.writerow(x)

new_row = {'nom': 'Lebaeaeaec', 'prenom': 'Buyob', 'date': '31/02/2010'}
add_to_csv(new_row, 'test.csv')


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