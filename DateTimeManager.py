# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 00:52:08 2018

@author: LENOVO
"""

import datetime

def getTodayDate():
    now = datetime.datetime.now()
    date = now.strftime("%Y%m%d")
    return date

def getTime():
    now = datetime.datetime.now()
    time = now.strftime("%H%M")
    return time

def getTodayDateTime():
    now = datetime.datetime.now()
    dateTime = now.strftime("%Y%m%d_%H%M")
    return dateTime


def timeDifference(time1,time2):
    format = "%H:%M"
    tdelta = datetime.datetime.strptime(time2,format) - datetime.datetime.strptime(time1,format)
    secondes = tdelta.seconds
    une_heure_en_secondes = 60 * 60
    heures = secondes / une_heure_en_secondes
    return heures

if __name__ == '__main__':
    print("[FILE::DateTimeManager][FCT::main]")