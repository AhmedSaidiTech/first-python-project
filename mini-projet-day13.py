# analyse de notes d'étudiants

import numpy as np

tab = np.array([
    ["      ","Math","Physique","Info"],
    ["Ahmed", 13.25    ,14,     10.25],
    ["Aymen", 15       ,15,        17]

])

notes=tab[1:,1:].astype(float) # récupérer seulement les notes pour faire les statistiques
print

print("liste des notes des étudiants \n")
print(tab)
print("les moyennes de chaque étudiant sont respectivement : \n")
print(np.mean(notes,axis=1)) # moyenne de chaque ligne
print("moyenne de classe pour chaque matiére respectivement sont : \n")
print(np.mean(notes,axis=0)) # moyenne de chaque colonne 

print("meilleur note pour chaque matiere : \n")
print(np.max(notes,axis=0))

print("plus petite note pour chaque matiere \n")
print(np.min(notes,axis=0))

print("l'écart-type des notes dans chaque matiere : \n")
print(np.std(notes,axis=0))

print("notes apres normalisation")
normalise = (notes - np.min(notes)) / (np.max(notes)-np.min(notes))
print(normalise)





