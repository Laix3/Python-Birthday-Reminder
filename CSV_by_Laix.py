import csv
import logging


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


def openFile(fichier):
    ''' Permet d'ouvrir un fichier csv et de convertir en dictionnaire
    in : exemple : file.csv
    out : dictionnaire du csv    
    '''
    try:
        file = open(fichier, 'r', encoding='utf8')

    except FileNotFoundError:
        logging.error('Fichier introuvable :/')
        print("Fichier introuvable :/")

    else:
        logging.info(f"Fichier, {fichier} ouvert")
        file = open(fichier, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=';')
        objets = [dict(ligne) for ligne in csv_en_dict]
    return objets


def add_to_csv(x,fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(x)
    print("Ajout effectué")
    logging.info(f"{x} écrit dans {fileName}")
    
    
def listCleanner(xList):
    ''' Permet d'enlever les '' d'un liste
    in : example : file.csv
    out : dictionnaire du csv    
    '''
    # verifie si c'est une liste
    if isinstance(xList, list):
        for i in xList:
            if i == '':
                xList.remove(i)
            else:
                pass
        logging.info("Fin du nettoyage de la liste :", xList)

        return xList
    
    else:
        return "Cleaner : Vous n'avez pas sélectionné une liste"