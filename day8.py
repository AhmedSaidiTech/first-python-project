# strings in python 

# slicing

texte = "MachineLearning"
print(type(texte))
print("les 7 premiers caracteres : ",texte[:8])
print("les 7 derniers caracteres : ",texte[8:])
print(texte[7:])
print("le premier carctere : ",texte[0])
print("le deriner caractere : ",texte[-1]) # l'indice -1 permet de récupérer le dernier carctere d"une chaine


# split : transform a string into a list 

texte = "I love football"

mots = texte.split()

print (mots)

print(type(mots))


# join : transform list of strings into one string 

mots = [ "I" , "Love" , "Football"]

text = " ".join(mots) 

print(text)

print(type(text))

# replace : permet de remplacer une partie de string 

phrase = "j'aime java "

phrase=phrase.replace("java","python")# strings can not be modified you should create another string to change to stocke the new value 

print(phrase)

# strip : delete the unusual spaces in the begining and the end of a string 

name = "   Ahmed   "

print(name)

nom = name.strip()

print("le nom sans espaces au début et fin est:",nom)

# F-strings : permet d'insérer des varibles dans un texte 

prénom = "ahmed"

age = 25

print (f"je m'appelle {prénom}  , j'ai {age} ans ")



