# numpy et matrices 

# une matrice numpy est simplement un tableau a plusieurs dimensions 

# création d'une matrice 

import numpy as np 

matrice =np.array([
    [12,14,16],
    [15,17,18],
    [10,8,7],
    [15,13,11]
])

print(matrice)
print("cest une matrice : ",matrice.shape)
print("nombre de lignes :",matrice.shape[0])
print("nombre de colonnes : ",matrice.shape[1])
print("c'est un tableau a",matrice.ndim,"dimensions")

# récupérer le 17 

print(matrice[1,1]) # indexation

# opérations vectorisés : notion trés importante dans le machine learning 

print (matrice+2)

print(matrice*2)

print(matrice/2)

print(matrice**2)

# opération entre les matrices 

A = np.array([
    [14,15],
    [10,7]
])

B= np.array([
    [17,12],
    [14,6]
])
print("résultat d'addition des matrices A et B : \n")
print(A+B)
print("résultat de multiplication élément par élement : \n")
print(A*B)
print("résultat de multiplication matricielle : \n")
print(A@B)
#ou bien
print(np.matmul(A,B))

# statistiques sur une matrice 

print(np.mean(A)) # moyenne de tous les éléments
print(np.max(A))  # l'element maximal
print(np.min(A))  # l'élément minimal
print(np.std(A))  # l'écart-type de la matrice 

print("moyenne par colonne : \n")

print(np.mean(A,axis=0))  # moyenne par colonne

print

print(np.mean(A,axis=1))  # moyenne par ligne 


# normalisation : rendre les valeurs en échelle comparable

min = np.min(A)
max= np.max(A)
normalise= (A - min)/(max-min)
print("aprés normalisation la matrice A devient : \n")
print(normalise)
