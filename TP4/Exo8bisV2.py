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

'''
    binomes = {}
    for i in range(0, len(etudiants) - 1, 2):  # Par pas de 2
        if i + 1 < len(etudiants):
            # Binôme normal (2 étudiants)
            binomes[f"binome_{i // 2 + 1}"] = [etudiants[i], etudiants[i + 1]]
        else:
            # Trinôme (dernier groupe impair)
            binomes[f"trinome_{i // 2 + 1}"] = [etudiants[i]]

    # Affichage final
    print("Les étudiants formants les binômes sont :")
    for id_groupe, groupe in binomes.items():
        for etu in groupe:
            print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")
'''

dictio()