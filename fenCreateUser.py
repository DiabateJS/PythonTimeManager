# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:26:55 2018

@author: LENOVO
"""

import tkinter as tk
import tkinter.ttk as ttk
import TextBdManager as tbm
import TextFileManager as tfm
import os

def onUserSelect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    userid = value.split("-")[0]
    user_data = getUserDataFromId(userid);
    IdUser.set(userid)
    NomUser.set(user_data["nomUser"])
    LoginUser.set(user_data["loginUser"])
    PwdUser.set(user_data["pwdUser"])
    ProfilUser.set(user_data["profilUserId"])
    label_resultat.config(text = "")
    
    
def deleteUserSelect():
    listbox_user_item_number = listbox_user.curselection()
    value = listbox_user.get(listbox_user_item_number)
    user_id = value.split("-")[0]
    user_name = value.split("-")[1]
    user_table_file_path = tbm.getTableFileName("User")
    table_users = tbm.selectAllDataFromTable("User")
    new_users_data = []
    for elt in table_users:
        tab = elt.split(";")
        if tab[0] != user_id:
            new_users_data.append(elt)
    os.remove(user_table_file_path)
    tfm.createTextFile(user_table_file_path)
    tfm.createTextFileWithContent(user_table_file_path,new_users_data)
    ClearFields()
    msg = "Utilisateur "+user_name+" supprimé avec succès !"
    label_resultat.config(text = msg)
    listbox_user.delete(listbox_user_item_number) 
    
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

def getNextUserId():
    tableUserData = tbm.selectAllDataFromTable("User")
    maxUserId = 0
    for pos in range(1,len(tableUserData)):
        ligne = tableUserData[pos]
        currentUserId = ligne.split(";")[0]
        if int(currentUserId) > maxUserId:
            maxUserId = int(currentUserId)
    maxUserId = maxUserId + 1;
    return formaterNbre(maxUserId,5)

def CreateUserInBase():
    oData = dict()
    nomUser = str(NomUser.get())
    nextUserId = getNextUserId()
    IdUser.set(nextUserId)
    oData["idUser"] = nextUserId
    oData["nomUser"] = nomUser
    oData["loginUser"] = str(LoginUser.get())
    oData["pwdUser"] = str(PwdUser.get())
    oData["profilUserId"] = str(ProfilUser.get())
    tbm.insertIntoTable("User",oData)
    ClearFields()
    msg = "Utilisateur "+str(nomUser)+" crée avec succès !"
    label_resultat.config(text = msg)
    new_line =  nextUserId + "-" + nomUser
    listbox_user.insert("end",new_line)
    
def ClearFields():
    IdUser.set("")
    NomUser.set("")
    LoginUser.set("")
    PwdUser.set("")
    ProfilUser.set("")
    label_resultat.config(text = "")
    
def chargerListeUsers():
    liste = tbm.selectAllDataFromTable("User")
    del liste[0]
    new_liste = []
    for elt in liste:
        tab = elt.split(";")
        id_user,nom_user = tab[0],tab[1]
        new_liste.append(id_user+"-"+nom_user)
    listbox_user.insert(tk.END, *new_liste)
    
def getUserDataFromId(id):
    table_users = tbm.selectAllDataFromTable("User")
    del table_users[0]
    user_data = dict()
    user_data["idUser"] = id
    for elt in table_users:
        tab = elt.split(";")
        if tab[0] == id:
            user_data["nomUser"] = tab[1]
            user_data["loginUser"] = tab[2]
            user_data["pwdUser"] = tab[3]
            user_data["profilUserId"] = tab[4]
    return user_data
    

fenetre = tk.Tk()
fenetre.geometry("600x500")
fenetre.title("Gestion des utilisateurs")

label_titre = tk.Label(fenetre, text="Gestion des utilisateurs",font="Arial 14 bold")
label_titre.grid(row=0,sticky='nesw',columnspan=3)

label_idUser = tk.Label(fenetre, text="Identifiant")
label_idUser.grid(column=0,row=1)

IdUser = tk.StringVar()
idUser = tk.Entry(fenetre, textvariable=IdUser,state="disabled")
idUser.grid(column=1,row=1,sticky='nesw',columnspan=3,pady=5,padx=5)

label_nomUser = tk.Label(fenetre, text="Nom")
label_nomUser.grid(column=0,row=2)

NomUser = tk.StringVar()
nomUser = tk.Entry(fenetre, textvariable=NomUser)
nomUser.grid(column=1,row=2,sticky='nesw',columnspan=3,pady=5,padx=5)

label_loginUser = tk.Label(fenetre, text="Login")
label_loginUser.grid(column=0,row=3,sticky='nesw')

LoginUser = tk.StringVar()
loginUser = tk.Entry(fenetre, textvariable=LoginUser)
loginUser.grid(column=1,row=3,sticky='nesw',columnspan=3,pady=5,padx=5)

label_pwdUser = tk.Label(fenetre, text="Password")
label_pwdUser.grid(column=0,row=4)

PwdUser = tk.StringVar()
pwdUser = tk.Entry(fenetre, textvariable=PwdUser,show='*')
pwdUser.grid(column=1,row=4,sticky='nesw',columnspan=3,pady=5,padx=5)

label_profil = tk.Label(fenetre, text="Profil")
label_profil.grid(column=0,row=5)

arProfil = ("0001","0002","0003","0004")
ProfilUser = tk.StringVar()
profilUser = ttk.Combobox(fenetre, state="readonly", values = arProfil, textvariable=ProfilUser)
profilUser.grid(column=1,row=5,sticky='nesw',columnspan=3,pady=5,padx=5)

label_resultat = tk.Label(fenetre, text="")
label_resultat.grid(column=0,row=6,sticky='nesw',columnspan=4)

bouton_creer = tk.Button(fenetre, text="Créer", command=CreateUserInBase)
bouton_creer.grid(column=0,row=7,sticky='nesw',pady=10,padx=10)

bouton_modifier = tk.Button(fenetre, text="Modifier", command=fenetre.quit)
bouton_modifier.grid(column=1,row=7,sticky='nesw',pady=10,padx=10)

#bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=fenetre.destroy)
bouton_effacer = tk.Button(fenetre, text="Effacer", command=ClearFields)
bouton_effacer.grid(column=2,row=7,sticky='nesw',pady=10,padx=10)

bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=deleteUserSelect)
bouton_supprimer.grid(column=3,row=7,sticky='nesw',pady=10,padx=10)

label_resultat = tk.Label(fenetre, text="Liste des utilisateurs crées",font="Arial 13 bold")
label_resultat.grid(column=0,row=8,sticky='nesw',columnspan=3)

listbox_user = tk.Listbox(fenetre)
listbox_user.bind('<<ListboxSelect>>', onUserSelect)
listbox_user.grid(column=0,row=9,sticky='nesw',columnspan=4)

chargerListeUsers()

fenetre.mainloop()
