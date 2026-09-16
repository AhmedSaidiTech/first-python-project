import json
print("je suis dans day9-ex.py")
etudiants = []

while True:
    print("---------------- Gestion des étudiants ----------------")
    print("1 - Ajouter un étudiant")
    print("2 - Afficher les étudiants")
    print("3 - Sauvegarder")
    print("4 - Charger")
    print("5 - Quitter")

    choix = int(input("Tapez votre choix : "))

    match choix:
        case 1:
            note = float(input("Note : "))

            while note < 0 or note > 20:
                print("Erreur : la note doit être entre 0 et 20.")
                note = float(input("Note : "))

            etudiant = {
                "nom": input("Donner le nom : "),
                "age": int(input("Donner l'âge de l'étudiant : ")),
                "note": note
            }

            etudiants.append(etudiant)
            print("Étudiant ajouté !")

        case 2:
            print("Affichage des étudiants")

            if len(etudiants) == 0:
                print("Aucun étudiant ajouté !")
            else:
                for etudiant in etudiants:
                    for cle, valeur in etudiant.items():
                        print(cle, ":", valeur)
                    print("----------------")

        case 3:
            print("Sauvegarde en cours")

            with open("etudiants.json", "w") as fichier:
                json.dump(etudiants, fichier, indent=4)

            print("Étudiants sauvegardés !")

        case 4:
            print("Chargement en cours")

            with open("etudiants.json", "r") as fichier:
                etudiants = json.load(fichier)

            print("Étudiants chargés !")

        case 5:
            print("Quitter")
            break

        case _:
            print("Choix invalide.")




