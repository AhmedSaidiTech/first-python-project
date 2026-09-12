# functions in python 

def average (notes) :
    return sum (notes) / len (notes)

def find_max (notes) :
    return max(notes)

def find_min (notes) :
    return min (notes)

def student_info (name , age , notes) :
    print ("nom de l'étudiant : ", name ,"\n" )
    print ("age de l'étudiant : ", age ,"\n" )
    print ("vos notes sont : \n")
    for i in notes :
     print (i,"\n")
    print ("ton note maximale est : \n",find_max(notes)) 
    print ("ton note minimale est : \n",find_min(notes))
    print ("ta moyenne est : \n", average(notes) )

# Remplissage de tableau de l'étudiant x et programme principale 

notes=[]

for i in range (1,5) :
  note = float(input(f"donner la {i} eme note : \n"))
  while note < 0 or note > 20 :
      print ("donner une note valide")
      note = float (input(f"donner la {i} eme note : \n"))
  notes.append(note)
      

student_info("Ahmed",25 , notes)






