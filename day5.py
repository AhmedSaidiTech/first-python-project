
# This program demonstrates the use of lists in Python.
# list contains 5 elements, which are printed using a for loop.
# we can remove and add elements to the list using the append() and remove() methods.

notes = [ 12 , 14 , 5 , 16 , 7 ]

for i in range ( 5 ) :
    print("" , i , ":" , notes[i])

notes.append(20)
notes.remove(5)

for i in range ( 5 ) :
    print("" , i , ":" , notes[i])


# tuples are similar to lists, but they are immutable, meaning that their elements cannot be changed after they are created.

coordonnes = ( 10.5 , 15 )

for i in range (2) :
 print("coordonnes : " , coordonnes [i])

# set is a collection of unique elements, which means that it cannot contain duplicate values. Sets are unordered, meaning that the elements do not have a specific order.

matieres = { "Maths" , "Physics" , "Chemistry" , "Biology" }
print("matieres : " , matieres)
matieres.add("English")
print("matieres : " , matieres) 

# dictionary is a collection of key-value pairs, where each key is unique and maps to a value.

etudiant = {
   "nom" : "Ahmed",
   "age" : 25 ,
   "height" : 1.78
   }

print("etudiant : " , etudiant)
print("nom : " , etudiant["nom"])   
etudiant["age"] = 26
etudiant["weight"]= 70 

print("etudiant : " , etudiant)

del(etudiant["height"])
del(etudiant["weight"])
etudiant["age"] -=1 

print("dictionary after updates \n", etudiant)