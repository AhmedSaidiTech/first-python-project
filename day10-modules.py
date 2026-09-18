# un module : un fichier python .py contenant de code a réutiliser 

import calculs #j'ai générer un fichier calculs.py contenant les fonctions arithmétiques de base ( + , / , - , *)

s= calculs.addition(10,13)
print("resultat de l'addition : ",s)

s= calculs.soustraction(10,13)
print("resultat de soustraction : ",s)

s= calculs.multiplication(10,13)
print("resultat de multiplication : ",s)

s=calculs.division(26,13)
print(type(s))  # résultat de division dans python est un float ! 
print("resulat de division :",s)