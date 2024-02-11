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

dates = []
for i in data:
    dates.append(i["date"])
    name = i["name"]


for date_anniversaire in dates:
    if date_anniversaire  == (datetime.date.today().strftime("%d/%m")):
        ctypes.windll.user32.MessageBoxW(0, f"C'est l'anniversaire de {name} aujourd'hui !", "Anniversaire", 1)
    else:
        quit()

ctypes.windll.user32.MessageBoxW(0, "END", "END", 1)
