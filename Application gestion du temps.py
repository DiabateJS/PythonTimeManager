# coding: utf-8
import matplotlib.pyplot as plt
import TextFileManager as tfm
import DateTimeManager as dtm


def getDateTimeDico(path):
	tab = tfm.readTextFile(path)
	dico = dict()
	for line in tab:
		if line != "":
			date,debutFin = line.split("::")
			debutFin = debutFin.replace("h",":")
			if "-" in debutFin:
				debut,fin = debutFin.split("-")
				dico[date] = debut,fin
	return dico


def getDureePerDayDico(path):
    dico = dict()
    dicoDateTime = getDateTimeDico(path)
    for cle in dicoDateTime.keys():
        debut,fin = dicoDateTime[cle]
        if (debut != '') and (fin != ''):
            dico[cle] = dtm.timeDifference(debut,fin)
    return dico

def incompleteDicoData(path):
    dc = getDateTimeDico(path)
    dc_incompleteData = dict()
    for cle in dc.keys():
        debut,fin = dc[cle]
        if (debut == '') or (fin == ''):
            dc_incompleteData[cle] = (debut,fin)
    return dc_incompleteData

def normalizeData(path):
    dc_duree_per_day = getDureePerDayDico(path)
    nb = len(dc_duree_per_day.keys())
    sum_values = 0
    for x in dc_duree_per_day.values():
        sum_values = sum_values + x
    mean_average = sum_values / nb
    dc_incomplete = incompleteDicoData(path)
    for cle in dc_incomplete.keys():
        dc_duree_per_day[cle] = mean_average
    return dc_duree_per_day


def getDataPlot(path):
    dc_days = normalizeData(path)
    x=dc_days.keys()
    x_finale = list()
    for libelle in x:
        jour,mois,annees = libelle.split("/")
        x_finale.append(jour+""+mois)
    y= dc_days.values()
    plt.plot(x_finale,y)
    plt.ylabel('Durée')
    plt.xlabel("Jours")
    plt.show()

if __name__ == '__main__':
    print("[FILE::Application gestion du temps][FCT::main]")
    timefilepath = "Arrivees_Departs.txt"
    getDataPlot(timefilepath)
    





    

