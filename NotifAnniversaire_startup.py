import logging
import ctypes

logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)

# FAIRE POUR CA CHECK SI C'EST LANNIVERSAIRE D'UNE PERSONNE


ctypes.windll.user32.MessageBoxW(0, "Text test", "Title test", 1)