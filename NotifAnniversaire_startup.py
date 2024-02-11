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

# Récupérer les dates d'anniversaire
dates_anniversaire = {personne["date"]: personne["prenom"] for personne in data}

# Vérifier si c'est l'anniversaire de quelqu'un aujourd'hui
anniversaires = [prenom for date, prenom in dates_anniversaire.items() if date == date_actuelle]

if anniversaires:
    message = "C'est l'anniversaire de : \n" + "\n".join(anniversaires)
    ctypes.windll.user32.MessageBoxW(0, message, "Anniversaires", 1)
else:
    ctypes.windll.user32.MessageBoxW(0, "Aucun anniversaire aujourd'hui.", "Fin", 1)