def dictio():
    etudiant1 = {
        "firstname": input("Entrez le prénom du premier étudiant : "),
        "name": input("Entrez le nom du premier étudiant : "),
        "promo": input("Entrez la promo du premier étudiant : "),
        "group": input("Entrez le groupe du premier étudiant : ")
    }

    etudiant2 = {
        "firstname": input("Entrez le second du premier étudiant : "),
        "name": input("Entrez le nom du second étudiant : "),
        "promo": input("Entrez la promo du second étudiant : "),
        "group": input("Entrez le groupe du second étudiant : ")
    }

    binome = {
        "binome1": etudiant1,
        "binome2": etudiant2
    }
    print("Les étudiants qui forment le binôme sont :")
    for i in binome:
        etudiant = binome[i]
        print(f"- L'étudiant {etudiant['name']} {etudiant['firstname']} du groupe {etudiant['group']}")
dictio()