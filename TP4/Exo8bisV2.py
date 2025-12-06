def dictio():
    nb_etudiant = int(input("Entrez le nombre d'étudiants que vous souhaitez entrez : "))
    etudiant = []
    for i in range(nb_etudiant):
        print(f"Etudiant {i+1}")
        firstname = input("Entrez le prénom du premier étudiant : ")
        name = input("Entrez le nom du premier étudiant : ")
        promo = input("Entrez la promo du premier étudiant : ")
        group = input("Entrez le groupe du premier étudiant : ")

        etudiant.append({
            "firstname": firstname,
            "name": name,
            "promo": promo,
            "group": group
        })

    if nb_etudiant % 2 == 0:
        binomes = []
        for i in range(0, nb_etudiant, 2):
            binome = (etudiant[i], etudiant[i + 1])
            binomes.append(binome)
            print(f"Le binôme {len(binomes)} est composé de {etudiant[i]['firstname']} {etudiant[i]['name']} et de {etudiant[i + 1]['firstname']} {etudiant[i + 1]['name']}")
    else:
        binomes = []
        trinome = []
        for i in range(0, nb_etudiant - 3, 2):
            binome = (etudiant[i], etudiant[i + 1])
            binomes.append(binome)
            print(f"Le binôme {len(binomes)} est composé de {etudiant[i]['firstname']} {etudiant[i]['name']} et de {etudiant[i + 1]['firstname']} {etudiant[i + 1]['name']}")
            trinome = (etudiant[-1],etudiant[-2], etudiant[-3])
            print(f"Le trinôme {len(binome)} est composé de {etudiant[-1]['firstname']} {etudiant[-1]['name']}, de {etudiant[-2]['firstname']} {etudiant[-2]['name']} et de {etudiant[-3]['firstname']} {etudiant[-3]['name']}")

dictio()