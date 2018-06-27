# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:24:44 2018

@author: LENOVO
"""

import TextFileManager as tfm
import random

def generateTestFile():
    
    calendrier = dict()

    annee = 2018
    calendrier["02"] = 31
    calendrier["02"] = 28
    calendrier["03"] = 31
    calendrier["04"] = 30
    calendrier["05"] = 31
    calendrier["06"] = 30

    fileName = "Arrivees_Departs.txt"
    arFileContent = []

    for mois in calendrier.keys():
        nbreJourDuMois = calendrier[mois]
        for jour in range(1,nbreJourDuMois):
            currentDay = str(jour)+"/"+str(mois)+"/"+str(annee)
            currentHeureDeb = "08h"+str(random.randint(0,59))
            currentHeureFin = "18h"+str(random.randint(15,59))
            arFileContent.append(currentDay+"::"+currentHeureDeb+"-"+currentHeureFin)

    tfm.createTextFileWithContent(fileName,arFileContent)

