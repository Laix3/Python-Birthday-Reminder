import ctypes
import datetime
import logging

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

    if jour_mois == date_actuelle:
        ctypes.windll.user32.MessageBoxW(0, f"Today is {x['fname']} {x['name']}'s birthday!", "Birthdays", 1)
        logging.info(f"Today is {x['fname']} {x['name']}'s birthday")
    
    else:
        quit()