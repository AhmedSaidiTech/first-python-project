# ojet orienté en python 

class etudiant :


    def __init__(self , nom , age , note) :
        self.nom=nom
        self.age=age
        self.note=note

    def afficher(self):
        print("Nom : ",self.nom)
        print("Age : ",self.age)
        print("Note: ",self.note)

    def est_admis(self):
        if(self.note>=10):
            print("résultat : admis")
        else :
            print("résultat: échec")

etudiant1 = etudiant("ahmed",25 ,15)

etudiant1.afficher()

# exercice du jour 11 : créér un modéle voiture , 2 objets de ce modele et faire un affichage pour chaque objet


class voiture : # classe voiture ou modele
   
   def __init__(self , marque , modele , annee ) :# constructeur de l'objet voiture 
       self.marque = marque
       self.modele=modele
       self.annee=annee


   def afficher (self) : # methode dans la classe voiture
       print ("marque : ", self.marque)
       print ("modele : ",self.modele)
       print("annee : ",self.annee)

voiture1 = voiture("Fiat","punto",2010) # création de 1 er objet de la classe voiture 
voiture2 = voiture("citroen","C3",2008) # création de 2 eme objet de la classe voiture
voiture1.afficher()# appelle a la methode afficher 
voiture2.afficher()