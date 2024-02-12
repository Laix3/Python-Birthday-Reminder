import csv
import logging


logging.basicConfig(
    filename='logs.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)


def openFile(x):
    ''' Opens a CSV file and converts it into a dictionary.
    in : example : file.csv
    out : dictionary of the CSV
    '''
    try:
        file = open(x, 'r', encoding='utf8')

    except FileNotFoundError:
        print(f"File {x} not found :/")

    else:
        print("File", x, "found !")
        file = open(x, 'r', encoding='utf8')
        csv_en_dict = csv.DictReader(file, delimiter=',')
        objets = [{k.lower(): v.lower() for k, v in ligne.items()} for ligne in csv_en_dict]
    return objets



def add_to_csv(x,fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        csvfile.write("\n")
        writer.writerow(x)
    print("Ajout de",x,"effectué")
    logging.info(f"{x} ecrit dans {fileName}")


    
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