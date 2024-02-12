import logging
import ctypes
import datetime
import csv


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)

def openFile(x):
    try:
        file = open(x, 'r', encoding='utf8')

    except FileNotFoundError:
        print(f"Fichier {x} introuvable :/")

    else:
        file = open(x, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=',')
        objets = [{k.lower(): v.lower() for k, v in ligne.items()} for ligne in csv_en_dict]
    return objets

data = openFile('data.csv')

date_actuelle = datetime.date.today().strftime("%d/%m")

for x in data:
    date = x['date']
    jour_mois = date.rsplit('/', 1)[0]

    if jour_mois == date_actuelle:
        ctypes.windll.user32.MessageBoxW(0, f"C'est l'anniversaire de {x['prenom']} {x['nom']} aujourd'hui !", "Anniversaires", 1)
        logging.info(f"C'est l'anniversaire de {x['prenom']} {x['nom']} aujourd'hui")
    
    else:
        quit()