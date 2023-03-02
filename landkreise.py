import csv
import matplotlib.pyplot as plt
import numpy as np

# Pfad zur Datenquelle
sourceFile = "./landkreis.csv"
# Zielpfad der Textdatei für Median und Mittelwert
targetFile = "./landkreise_mittelwert_median.txt"


# Aufgabe 2
def readData(_file):
    """ Funktion liest Daten aus CSV-Datei ein und gibt diese als Dictionary zurück """
    # Dictionary zur Speicherung der Landkreise und deren Fläche
    landkreise = {}

    # iteriert über alle Zeilen der CSV-Datei
    with open(_file, encoding="latin-1") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            # prüft, ob Zeile mit fünfstelliger Ziffer beginnt
            if row[0].isnumeric() and len(row[0]) == 5:
                # fügt Zeile zu Dictionary hinzu
                landkreise[row[1]] = row[2]

    # gibt die Landkreise und deren Fläche als Dictionary zurück
    return landkreise


def sortDict(dictionary):
    """ Funktion sortiert Elemente in einem Dictionary basierend auf den Values """
    # temporäres Dictionary
    dictTemp = {}

    # Schleife fügt die Werte aus dem übergebenen Dictionary dem temporären Dictionary hinzu
    for key, value in dictionary.items():
        # prüft, ob Fläche eines Landkreises leer ist
        if not value.__contains__('-'):
            # fügt Daten als float zum temporären Dictionary hinzu
            dictTemp[key] = float(value.replace(',', '.'))

    # sortiert die Werte der Größe nach und gibt das temporäre Dictionary zurück
    return dict(sorted(dictTemp.items(), key=lambda x: x[1], reverse=False))


# Aufgabe 3
def calcAverageAndMedian(dictionary):
    """ Funktion berechnet Mittelwert und Median aus den übergebenen Werten des Dictionary's """
    # sortiert die Werte der Größe nach
    dictTempSorted = sortDict(dictionary)

    """ Mittelwert berechnen """
    average = 0.0
    # Summiert alle Werte
    for i in dictTempSorted.values():
        average += i
    # teilt die Summer aller Werte durch die Anzahl der Werte und rundet auf zwei Nachkommastellen
    average = round((average / len(dictTempSorted)), 2)

    """ Median berechnen """
    # speichert mittleren Wert
    mid = (len(dictTempSorted) - 1) // 2
    # prüft, ob Anzahl der Werte gerade oder ungerade ist
    if len(dictTempSorted) % 2:
        # Anzahl der Werte ungerade: mittlerer Wert ist Median
        median = list(dictTempSorted.values())[mid]
    else:
        # Anzahl der Werte gerade: mitte der beiden mittleren Werte ist Median
        median = (list(dictTempSorted.values())[mid] + list(dictTempSorted.values())[mid + 1]) / 2.0

    """ Mittelwert und Median in Datei schreiben """
    # versucht Datei zu öffnen
    try:
        f = open(targetFile, "w")
        # versucht in Datei zu schreiben
        try:
            f.write("Mittelwert: " + str(average) + "\n" + "Median: " + str(median))
        # wirft Fehler, wenn Datei nicht beschrieben werden kann
        except:
            print("In die Datei konnte keine Werte geschrieben werden.")
        # schließt Datei
        finally:
            f.close()
    # wirft Fehler, wenn Datei nicht erzeugt oder geöffnet werden konnte
    except:
        print("Die Datei " + targetFile + " konnte nicht erzeugt werden")

    # gibt Mittelwert und Median als Liste zurück
    return [average, median]


# Aufgabe 4
def getSmallestAndBiggest(d):
    """ Funktion gibt die zehn größten und kleinsten Landkreise mit deren Flächen zurück """
    # sortiert das übergebene Dictionary
    dictTempSorted = sortDict(d)
    # Dictionary für die zehn kleinsten Landkreise
    smallest10 = {}
    # Dictionary für die zehn größten Landkreise
    biggest10 = {}

    # fügt die zehn kleinsten Landkreise zum Dictionary hinzu
    for i in range(len(dictTempSorted)):
        if i < 10:
            smallest10[list(dictTempSorted.keys())[i]] = list(dictTempSorted.values())[i]

    # fügt die zehn größten Landkreise zum Dictionary hinzu
    for i in range(len(dictTempSorted)):
        if i > len(dictTempSorted) - 10:
            biggest10[list(dictTempSorted.keys())[i]] = list(dictTempSorted.values())[i]

    # gibt die zehn größten und zehn kleinsten Landkreise als Liste zurück
    return [smallest10, biggest10]


# Aufgabe 5
def showDiagramms(smallest, biggest, allElement):
    """ Funktion zeigt Diagramme für die kleinsten, größten und alle Landkreise """
    # erstellt x- und y-Achse mit jeweiligen Werten
    xSmallest = np.array(list(smallest.keys()))
    ySmallest = np.array(list(smallest.values()))
    xBiggest = np.array(list(biggest.keys()))
    yBiggest = np.array(list(biggest.values()))
    xAll = np.array(list(allElement.keys()))
    yAll = np.array(list(allElement.values()))

    # fügt Beschriftung der Achsen hinzu
    plt.xlabel('Fläche (in qkm)')
    plt.ylabel('Landkreis')

    # erzeugt Balkendiagramm für die zehn kleines Landkreise
    plt.title("Zehn kleinsten Landkreise")
    plt.barh(xSmallest, ySmallest)
    plt.show()

    # fügt Beschriftung der Achsen hinzu
    plt.xlabel('Fläche (in qkm)')
    plt.ylabel('Landkreis')

    # erzeugt Balkendiagramm für die zehn größten Landkreise
    plt.title("Zehn größten Landkreise")
    plt.barh(xBiggest, yBiggest)
    plt.show()

    # fügt Beschriftung der Achsen hinzu
    plt.xlabel('Fläche (in qkm)')
    plt.ylabel('Landkreise')

    # erzeugt Balkendiagramm für alle Landkreise
    plt.title("Alle Landkreise")
    plt.tick_params(left=False, labelleft=False)
    plt.barh(xAll, yAll)
    plt.show()


landkreiseDict = readData(sourceFile)
averageAndMedian = calcAverageAndMedian(landkreiseDict)
smallestAndBiggest = getSmallestAndBiggest(landkreiseDict)
showDiagramms(smallestAndBiggest[0], smallestAndBiggest[1], sortDict(landkreiseDict))
