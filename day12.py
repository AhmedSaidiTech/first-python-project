import numpy as np  # np est simplement un raccourci pour écrire numpy directement 

notes=np.array([10 , 14 , 16 , 18 ]) 

print (notes.ndim) # c'est un tableau 1D 

print (type(notes))

print(notes)

print(notes+2)

# indexing ( récupérer un element de tableau )

print(notes[0]) # premier element

print(notes[-1]) # dernier element 

# shape : indique la forme de tableau 

print(notes.shape) # (4,) 4 colonnes 

notes = np.array([[10 , 14 , 16 , 18 ], # ndarry 2 dimensions : ligne et colonne 
                 
                 [14 , 16 , 19 , 20],
                 
                 [18 , 19 , 20 ,14]])

print(type(notes))

print(notes)

print(notes+2)

print(notes.shape) # (2,4) : (2 lignes , 4 colonnes )

print(notes.ndim) # connaitre le nombre de dimension 2D : ligne et colonne 

print(notes[0,2])

print(notes[-1,-1]) #dernier element 


# slicing : récupérer une partie de tableau 

print(notes[0:2,0:2]) # récupere les 2 premieres lignes et les 2 premiers colonnes

print(np.sum(notes)) # calculer la somme 

print(np.mean(notes)) # calculer la moyenne  

print(np.min(notes)) # afficher le minimum

print(np.max(notes)) # afficher le maximum 

print(np.std(notes)) # afficher l'écart-type 

      








