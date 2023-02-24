import csv
import matplotlib.pyplot as plt
import numpy as np

sourceFile = "./landkreis.csv"
targetFile = "./landkreise_mittelwert_median.txt"


def readData(_file):
    landkreise = {}
    with open(_file, encoding="latin-1") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[0].isnumeric() and len(row[0]) == 5:
                landkreise[row[1]] = row[2]
    return landkreise


def calcAverageAndMedian(dictionary):
    """ Funktion berechnet Mittelwert und Median aus den übergebenen Werten des Dictionary's """

    # Schleife fügt die Werte aus dem übergebenen Dictionary der Liste hinzu
    values = []
    for i in dictionary.values():
        # prüft, ob Fläche eines Landkreises leer ist
        if not i.__contains__('-'):
            # fügt den Wert als Float zur Liste hinzu
            values.append(float(i.replace(',', '.')))
    # sortiert die Werte der Größe nach
    values.sort()

    """ Mittelwert berechnen """
    average = 0.0
    # Summiert alle Werte
    for i in values:
        average += i
    # teilt die Summer aller Werte durch die Anzahl der Werte und rundet auf zwei Nachkommastellen
    average = round((average / len(values)), 2)

    """ Median berechnen """
    # speichert mittleren Wert
    mid = (len(values) - 1) // 2
    # prüft, ob Anzahl der Werte gerade oder ungerade ist
    if len(values) % 2:
        # Anzahl der Werte ungerade: mittlerer Wert ist Median
        median = values[mid]
    else:
        # Anzahl der Werte gerade: mitte der beiden mittleren Werte ist Median
        median = (values[mid] + values[mid + 1]) / 2.0

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


def getSmallestAndBiggest(d):
    # Schleife fügt die Werte aus dem übergebenen Dictionary der Liste hinzu
    values = []
    for i in d.values():
        # prüft, ob Fläche eines Landkreises leer ist
        if not i.__contains__('-'):
            # fügt den Wert als Float zur Liste hinzu
            values.append(float(i.replace(',', '.')))
    # sortiert die Werte der Größe nach
    values.sort()

    smallest10 = []
    for i in range(10):
        smallest10.append(values[i])

    biggest10 = []
    for i in range(len(values) - 1, len(values) - 11, -1):
        biggest10.append(values[i])

    return [smallest10, biggest10]


def showDiagramm(smallest, biggest):
    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x, y)
    plt.show()


landkreiseDict = readData(sourceFile)
averageAndMedian = calcAverageAndMedian(landkreiseDict)
smallestAndBiggest = getSmallestAndBiggest(landkreiseDict)
showDiagramm(smallestAndBiggest[0], smallestAndBiggest[1])
