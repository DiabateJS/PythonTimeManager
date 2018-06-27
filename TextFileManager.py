# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:26:23 2018

@author: LENOVO
"""
import os
import DateTimeManager as dtm

def createTextFile (path):
    file = open(path,'w')
    file.close()

def createTextFileWithCalculatedPath (path):
	now = dtm.getTodayDateTime()
	totalPath = path+os.sep+now+".txt"
	createTextFile(totalPath)
    
def createTextFileWithContent(filePath,listContent):
    f= open(filePath,"w+")
    for ligne in listContent:
        f.write(ligne+"\n")
    f.close()

def insertLineInTextFile(filePath,line):
    fileContent = readTextFile(filePath)
    fileContent.append(line)
    createTextFileWithContent(filePath,fileContent)

def deleteFile(filePath):
    os.remove(filePath)
	
def readTextFile (path):
	with open(path) as contents:
		datas = contents.readlines()
		data = []
		for line in datas:
			data.append(line.replace('\n',''))
	return data

if __name__ == '__main__':
    print("[FILE::TextFileManager][FCT::main]")
