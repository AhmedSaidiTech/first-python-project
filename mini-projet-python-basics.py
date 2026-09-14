# partie 1 : informations de l'étudiant 

name = str ( input (" nom de l'étudiant : "))

age = int ( input ("Age : "))

# partie 2 : saisi des notes de l'étudiant 

nb_notes = int ( input ("combien de notes voulez vous entrer ? "))

notes =[]

for i in range ( 1 , nb_notes +1 ) : 
  
 note = float ( input (f"donner la {i} eme note : \n"))
 

 while ( note < 0) or ( note > 20) :

   note = float ( input ( f"donner la {i} eme note : \n" ))
 
 notes.append(note)
 

# Partie 3 :  Affichage des notes ( les notes sont stockés dans la liste notes )

def affiche_notes(notes , nb_notes , name):

 print ( "Notes de : " , name)

 for i in  range  (nb_notes) : # une liste commence par l'index 0 et pas 1 donc range (1 ,... ) est faux !
 
  print ( " Note ",i+1, " : ", notes[i] ,"\n")

# Partie 4 : Calcul de la moyenne de l'étudiant

def calculer_moyenne(notes) :

 moy = sum(notes)/len(notes)

 print ( " Moyenne : ",moy)

 return moy 

# Partie 5 : vérification de réussite 

def verif(moy) :
 
 print ( " Moyenne : ",moy , "\n")

 if ( moy >=10):
  print ("Résultat : Admis")
 else:
  print ("Résultat : Réfusé")

# Partie 6 : La meilleure note et la plus mauvaise note 

def stats1 (notes) :

 print ("La meilleure note  : ", max(notes) , "\n")

 print ("la mauvaise note : " , min(notes))


# Partie 7 : nombre de notes >= 10 et nombre de notes < 10 

def stats2 (notes) :

 nb_sup_10 = 0 

 nb_inf_10 = 0 

 for i in notes : 
  if (i >= 10) :
   nb_sup_10 +=1
 else :
   nb_inf_10 +=1

 print ("nombre de notes ayant la moyenne est : ",nb_sup_10 ,"\n")

 print ("nombre de notes inférieures a 10 est : " , nb_inf_10)

# Partie 8 : Dictionnaire de l'étudiant (optionel dans l'affichage )

def affichage_info( moy , name , age  ) : 

 etudiant = {
   "nom" : name ,

   "age ": age , 

   "moyenne " : moy ,

   "résultat" : verif(moy)
 }

 for cle , valeur in etudiant.items() :
  print (cle,":", valeur)
 

# Partie 9 : définir les fonctions nécessaires pour les appeler dans le programme principal 


print ("--------------------------Gestion des notes ------------------------------------------------------ \n")

print ("nom de l'étudiant : ",name ,"\n")

print ("age : ",age ,"ans \n")


print ("----------------------------Résultat-------------------------------------------------------------------------")

affiche_notes(notes , nb_notes , name)

moy = calculer_moyenne(notes)

stats1(notes)

stats2(notes)

verif(moy)















     


