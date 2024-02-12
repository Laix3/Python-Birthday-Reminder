import logging
import ctypes
import datetime

from CSV_by_Laix import openFile

logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


data = openFile('data.csv')

date_actuelle = datetime.date.today().strftime("%d/%m")

for x in data:
    date = x['date']
    jour_mois = date.rsplit('/', 1)[0]
    print(jour_mois)
    if jour_mois == date_actuelle:
        ctypes.windll.user32.MessageBoxW(0, f"C'est l'anniversaire de {x['prenom']} {x['nom']} aujourd'hui", "Anniversaires", 1)
    
    else:
        quit()