# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:41:37 2018

@author: LENOVO
"""

import TextFileManager as tfm
import os.path

def getTablesEntetes():
    dcTable = dict() 
    dcTable["User"] = ["idUser","nomUser","loginUser","pwdUser","profilUserId"]
    dcTable["Projet"] = ["idProjet","libProjet","descProjet","idChefProjet","dureeEstimee","dureeReelle","etatAvancement","dateDebut","dateFin"]
    dcTable["Tache"] = ["idTache","idProjet","libTache","idUsers","dureeEstimee","dureeTotale","etatAvancement","tauxRealisation","dateDebut","dateFin"]
    dcTable["UserProfil"] = ["profilId","libProfil","droits"]
    dcTable["Droit"] = ["idDroit","item"]
    dcTable["Compteur"] = ["idCompteur","libCompteur","nbreCar"]
    return dcTable

def getTableFileName(tableName):
    return tableName+"_bd.txt"
    
def createDbFiles():
    dcTableBd = getTablesEntetes() 
    
    for table in dcTableBd.keys():
        arCurrentEnTete = [";".join(dcTableBd[table])]
        tableFileName = getTableFileName(table)
        if (os.path.exists(tableFileName) == False):
            tfm.createTextFileWithContent(tableFileName,arCurrentEnTete)
        
def insertIntoTable(tableName,dcData):
    lineToInsert = ";".join(dcData.values())
    tableFileName = getTableFileName(tableName)
    tfm.insertLineInTextFile(tableFileName,lineToInsert)
    
def selectAllData():
    dcTableEntetes = getTablesEntetes()
    dcAllData = dict()
    for cle in dcTableEntetes.keys():
        tableFileName = getTableFileName(cle)
        dcAllData[cle] = tfm.readTextFile(tableFileName)
    return dcAllData

def selectAllDataFromTable(tableName):
    tableFileName = getTableFileName(tableName)
    if (os.path.exists(tableFileName)):
        return tfm.readTextFile(tableFileName)
    return []

def selectAllDataByTableColumn(tableName,columnName):
    arTableData = selectAllDataFromTable(tableName)
    arEntetes = arTableData[0]
    if (columnName in arEntetes):
        indice = arEntetes.index(columnName)
        arColData = []
        for pos in range(1,len(arEntetes)-1):
            arColData.append(arEntetes[pos].split(";")[indice])
        return arColData
    return []
        
if __name__ == '__main__':
    print("[FILE::TextBdManager][FCT::main]")
    createDbFiles()
        
