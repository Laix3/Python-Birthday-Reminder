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
    print("Addition of", x, "completed")
    logging.info(f"{x} written in {fileName}")


    
def listCleanner(xList):
    ''' Removes empty strings from a list.
    in : example : file.csv
    out : dictionary of the csv
    '''
    # verifie si c'est une liste
    if isinstance(xList, list):
        for i in xList:
            if i == '':
                xList.remove(i)
            else:
                pass
        logging.info("List cleaning complete :", xList)

        return xList
    
    else:
        return "Cleaner: You did not select a list"