import ctypes
import datetime
import logging
import csv
from plyer import notification


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


def openFile(x):
    try:
        file = open(x, 'r', encoding='utf8')

    except FileNotFoundError:
        print(f"[*] File {x} not found :/")

    else:
        file = open(x, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=',')
        objets = [{k.lower(): v.lower() for k, v in ligne.items()} for ligne in csv_en_dict]
    return objets


data = openFile('data.csv')

date_actuelle = datetime.date.today().strftime("%d/%m")


for i in data:

    jour_mois = (i['date'].rsplit('/', 1)[0])

    if jour_mois == str(date_actuelle):
        
        notification.notify(
        app_icon = "Images/cake.ico",
        title = "Birthdays",
        message = f"Today is {i['fname']} {i['name']}'s birthday !",
        timeout = 20
        )
        
        ctypes.windll.user32.MessageBoxW(0, f"Today is {i['fname']} {i['name']}'s birthday !", "Birthdays", 1)
        logging.info(f"Today is {i['fname']} {i['name']}'s birthday")
        
        quit()
        
        
    else:
        pass

notification.notify(
app_icon = "Images/no-cake.ico",
title = "No Birthdays",
message = "No birthday today",
timeout = 10
)