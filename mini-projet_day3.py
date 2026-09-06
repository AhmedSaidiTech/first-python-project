note_algo = float ( input ("saisir une note" ))

note_python = float ( input ("saisir une note" ))


note_bd = float ( input ("saisir une note" ))

moy = (note_algo + note_python + note_bd) / 3

if moy >= 16 and moy <= 20 :
    print (f"votre moyenne est {moy} vous avez la mention très bien")
elif moy >= 14 :
    print (f"votre moyenne est {moy} vous avez la mention bien")
elif moy >= 12 :
    print (f"votre moyenne est {moy} vous avez la mention assez bien")
elif moy >= 10 :
    print (f"votre moyenne est {moy} vous avez la mention passable")
elif moy < 10 :
    print (f"votre moyenne est {moy} vous avez échoué !")
else :
    print ("erreur de saisie")




