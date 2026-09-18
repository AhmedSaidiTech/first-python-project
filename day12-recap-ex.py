import numpy as np

notes= np.array([12,15,16,17,16,11,8])

print("--------------------------------Analyse de notes------------------------------------------------------\n")

print ("Notes : ", notes )

print ("nombre de notes : ", notes.shape)

print("moyenne : ",np.sum(notes)/np.shape(notes))

print("note minimal : ",np.min(notes))

print("note maximale : ",np.max(notes))

print("somme :",np.sum(notes))

print("ecart-type : ",np.std(notes))

print("les 5 premiers notes : ",notes[:5])


