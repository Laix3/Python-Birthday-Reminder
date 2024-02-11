import os
import shutil
import sys
import logging

from NotifAnniversaire import openFile,add_Wstartup,remove_Wstartup


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)

# FAIRE POUR CA CHECK SI C'EST LANNIVERSAIRE D'UNE PERSONNE