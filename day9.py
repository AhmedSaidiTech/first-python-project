# files in python 

# create and read a file content 

# 1 st  method : oepn -> write -> close -> open again -> read -> close 

fichier = open("test.txt","w")
fichier.write("Bonjour , ceci est mon fichier")
fichier.close()
fichier = open("test.txt","r")
contenu=fichier.read()
print(contenu)

fichier.close()

# 2 nd method : we use with to close automatically the file and seek() function to start reading the file from the begining apres la fermeture de fichier 

with open ("test.txt","w+") as fichier :
    fichier.write("bonjour wilsis makatek , nathaninbadjou")
    fichier.seek(0)
    contenu=fichier.read()
    fichier.seek(0)# You need to move the cursor back to the beginning of the file because after each read or write, the cursor is at the end. 
    lignes=fichier.readlines() 
    print(contenu)
    print(lignes)


with open ("test.txt " , "w+") as fichier :
    fichier.write("banjourat \n")
    fichier.write("wislsis makatek\n")
    fichier.write("ywazzzaa3\n")
    fichier.seek(0)
    contenu=fichier.read()
    print ("contenu de fichier : ", contenu)
    fichier.seek(0)
    lignes=fichier.readlines()
    print("la liste des lignes de fichier : \n",lignes)

# add new ligne to the file without deleting the old content 

with open("test.txt","a+") as fichier: #a+ : add + read // a : add only 
    fichier.write("dramateng shoot")
    fichier.seek(0)
    contenu = fichier.read()
    print (contenu)


# csv file in python : comma -separated values 

# create + write a csv file 

import csv 

with open ("etudiant.csv","w",newline="") as fichier :
    writer = csv.writer(fichier)

    writer.writerow(["nom","age","ville"])
    writer.writerow(["Ali",22,"Paris"])
    writer.writerow(["Yassine",30,"Marseille"])

# read the csv file 

with open ("etudiant.csv","r") as fichier :

    reader = csv.reader(fichier)
    print (reader)# affiche un objet et pas le contenu de fichier 
    for ligne in reader :
        print(ligne) # affiche le contenu aussi on peut utiliser readlines()

# json file : usually used to structured data 

# creating and writing the json file

import json 

etudiant = {
    "nom" : "ahmed",
    "age" : 25 ,
    "note": 15 
}

with open ("etudiant.csv","w") as fichier :
    json.dump(etudiant , fichier , indent=4)# indent = 4 make the file more clear and readable

# reading the json file 

with open ("etudiant.csv","r") as fichier :
    etudiant = json.load(fichier) # load ! 
print (etudiant)
print(etudiant["nom"])
print(etudiant["age"])



           






           

