etudiants = {
  "Ahmed" : [12 , 14 , 18 , 11] ,
  "Ali"   : [11 , 10.5 , 12 ,13],
  "Arij"  : [15 , 16 , 17 , 18],
  "Siwar" : [12 ,14 , 18 , 11], 
  "Aymen" : [20 ,20 , 20 , 19.75]

}


print ("----------------------------------Gestion de notes --------------------------------------------------------\n")

for cle in etudiants.keys() :
    print (cle)

    print ("la moyenne de " , cle , "est : ", sum(etudiants[cle])/len(etudiants[cle]))

    if (sum(etudiants[cle])/len(etudiants)) >= 10 :
        print ( "statut : Admis \n----------------------------------------------------")
    else :
        print ( "statut : refusé \n -------------------------------------------------")

        



