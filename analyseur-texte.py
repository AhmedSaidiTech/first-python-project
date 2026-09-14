from collections import Counter 

# collections est un module python , un module est une boite a outils qui contient du code déja prét . pour utiliser un outil d'un module , on fait import
# depuis le module collections je veux utiliser l'outil Counter ( C majuscule ! ) il compte automatiquement la frequence de chaque element dans une liste 
# on doit transformer le texte en liste de mots avec le split pour appliquer le Counter de module collections
# tapez un texte

phrase = str (input ("donner une phrase "))

# compter le nombre de cracteres

nb_char =0 

nb_mots = 0

for i in phrase :
    nb_char+=1
print ("nombre de caracteres : " , nb_char)  

mots = phrase.split()

for i in mots :
    nb_mots +=1

print ("nombre de mots " ,nb_mots)
print("liste de mots :  \n ")
for i in mots :
    print (i)

print("fréquence des mots : \n")
words = phrase.split()
compteur=Counter(words)
print(compteur)
print(type(compteur))

for mot , nb in compteur.items() :
    print ( "fréquence de mot ",mot ,":",nb)








