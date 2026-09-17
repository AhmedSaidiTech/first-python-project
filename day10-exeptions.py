# try pour tester un code 

# exept pour gérer l'erreur

# finally : s'éxecute dans tous les cas 


# exemple d'execption : saisi des nombre + division par 0 

try :
    a = int (input("danner un entier \n"))
    b=  int (input("donner un entier \n"))
    resultat = a / b 
    print("résultat = ",resultat)

except ValueError :
    print("Erreur : entrer uniquement des nombres!")

except ZeroDivisionError :
    print("Erreur : b doit etre noon nulle !")

finally :
    print("programme terminé !")


