# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:16:28 2018

@author: jsdiabate
"""

import tkinter as tk
import tkinter.ttk as ttk
import TextBdManager as tbm
import TextFileManager as tfm
import os

def onProfilSelect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    userProfilId = value.split("-")[0]
    userProfil_data = getUserProfilDataFromId(userProfilId);
    IdProfil.set(userProfilId)
    LibelleProfil.set(userProfil_data["libProfil"])
    
    label_resultat.config(text = "")
    
    
def deleteUserProfilSelect():
    listbox_profil_item_number = listbox_profil.curselection()
    value = listbox_profil_item_number.get(listbox_profil_item_number)
    profil_id = value.split("-")[0]
    lib_profil = value.split("-")[1]
    user_table_file_path = tbm.getTableFileName("UserProfil")
    table_userProfil = tbm.selectAllDataFromTable("UserProfil")
    new_usersProfil_data = []
    for elt in table_userProfil:
        tab = elt.split(";")
        if tab[0] != profil_id:
            new_usersProfil_data.append(elt)
    os.remove(user_table_file_path)
    tfm.createTextFile(user_table_file_path)
    tfm.createTextFileWithContent(user_table_file_path,new_usersProfil_data)
    ClearFields()
    msg = "Profil : "+lib_profil+" supprimé avec succès !"
    label_resultat.config(text = msg)
    listbox_profil.delete(listbox_profil_item_number)
    
def formaterNbre(val,nbreCar):
    sVal = str(val)
    ecart = nbreCar - len(sVal)
    sEcart = ""
    if (ecart > 0):
        for l in range(0,ecart):
            sEcart = sEcart + "0"
        return sEcart + sVal
    else:
        return "00001"

def getNextProfilId():
    tableUserProfilData = tbm.selectAllDataFromTable("UserProfil")
    maxProfilId = 0
    for pos in range(1,len(tableUserProfilData)):
        ligne = tableUserProfilData[pos]
        currentUserProfilId = ligne.split(";")[0]
        if int(currentUserProfilId) > maxProfilId:
            maxProfilId = int(currentUserProfilId)
    maxProfilId = maxProfilId + 1;
    return formaterNbre(maxProfilId,4)

def CreateUserProfilInBase():
    oData = dict()
    libProfil = str(LibelleProfil.get())
    nextProfilId = getNextProfilId()
    IdProfil.set(nextProfilId)
    oData["profilId"] = nextProfilId
    oData["libProfil"] = libProfil
    oData["droits"] = ""
    tbm.insertIntoTable("UserProfil",oData)
    ClearFields()
    msg = "Profil "+str(libProfil)+" crée avec succès !"
    label_resultat.config(text = msg)
    new_line =  nextProfilId + "-" + libProfil
    listbox_profil.insert("end",new_line)
    
def ClearFields():
    IdProfil.set("")
    LibelleProfil.set("")
    label_resultat.config(text = "")
    
def chargerListeProfils():
    liste = tbm.selectAllDataFromTable("UserProfil")
    del liste[0]
    new_liste = []
    for elt in liste:
        tab = elt.split(";")
        id_profil,nom_profil = tab[0],tab[1]
        new_liste.append(id_profil+"-"+nom_profil)
    listbox_profil.insert(tk.END, *new_liste)
    
def getUserProfilDataFromId(id):
    table_userProfil = tbm.selectAllDataFromTable("UserProfil")
    del table_userProfil[0]
    userProfil_data = dict()
    userProfil_data["profilId"] = id
    for elt in table_userProfil:
        tab = elt.split(";")
        if tab[0] == id:
            userProfil_data["libProfil"] = tab[1]
            userProfil_data["droits"] = tab[2]
    return userProfil_data
    

fenetre = tk.Tk()
fenetre.geometry("600x500")
fenetre.title("Gestion des profils utilisateurs")

label_titre = tk.Label(fenetre, text="Gestion des profils utilisateurs",font="Arial 14 bold")
label_titre.grid(row=0,sticky='nesw',columnspan=3)

label_idProfil = tk.Label(fenetre, text="Id Profil")
label_idProfil.grid(column=0,row=1)

IdProfil = tk.StringVar()
idProfil = tk.Entry(fenetre, textvariable=IdProfil,state="disabled")
idProfil.grid(column=1,row=1,sticky='nesw',columnspan=3,pady=5,padx=5)

label_libelleProfil = tk.Label(fenetre, text="Libelle Profil")
label_libelleProfil.grid(column=0,row=2)

LibelleProfil = tk.StringVar()
libelleProfil = tk.Entry(fenetre, textvariable=LibelleProfil)
libelleProfil.grid(column=1,row=2,sticky='nesw',columnspan=3,pady=5,padx=5)

label_loginUser = tk.Label(fenetre, text="Droits du profil",font="Arial 12 bold")
label_loginUser.grid(row=3,sticky='nesw',columnspan=3)

label_resultat = tk.Label(fenetre, text="")
label_resultat.grid(column=0,row=4,sticky='nesw',columnspan=4)

bouton_creer = tk.Button(fenetre, text="Créer", command=CreateUserProfilInBase)
bouton_creer.grid(column=0,row=5,sticky='nesw',pady=10,padx=10)

bouton_modifier = tk.Button(fenetre, text="Modifier", command=fenetre.quit)
bouton_modifier.grid(column=1,row=5,sticky='nesw',pady=10,padx=10)

#bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=fenetre.destroy)
bouton_effacer = tk.Button(fenetre, text="Effacer", command=ClearFields)
bouton_effacer.grid(column=2,row=5,sticky='nesw',pady=10,padx=10)

bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=deleteUserProfilSelect)
bouton_supprimer.grid(column=3,row=5,sticky='nesw',pady=10,padx=10)

label_resultat = tk.Label(fenetre, text="Liste des profils crées",font="Arial 11 bold")
label_resultat.grid(column=0,row=6,sticky='nesw',columnspan=3)

listbox_profil = tk.Listbox(fenetre)
listbox_profil.bind('<<ListboxSelect>>', onProfilSelect)
listbox_profil.grid(column=0,row=9,sticky='nesw',columnspan=4)

chargerListeProfils()

fenetre.mainloop()