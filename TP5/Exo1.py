def operation():
    nom1 = input("Nom de la personne 1 : ")
    prenom1 = input("Prenom de la personne 1 : ")

    nom2 = input("Nom de la personne 2 : ")
    prenom2 = input("Prenom de la personne 2 : ")

    p1 = prenom1.capitalize() + " " + nom1.upper()
    p2 = prenom2.capitalize() + " " + nom2.upper()

    if nom1.lower() < nom2.lower() or (nom1.lower() == nom2.lower() and prenom1.lower() < prenom2.lower()):
        print(p1)
        print(p2)
    else:
        print(p2)
        print(p1)

operation()
