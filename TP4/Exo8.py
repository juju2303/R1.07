def dictio():
    etudiant1 = {
        "firstname": "jules",
        "name": "landauer",
        "promo": "2025-2026",
        "group": "122"
    }

    print(f"votre nom est {etudiant1['name']}, votre prénom est {etudiant1['firstname']}, "
          f"vous faites partie de la promo {etudiant1['promo']} et votre groupe est le {etudiant1['group']}")


    print(f"Les clés du dictionnaire sont :")
    for i in etudiant1.keys():
        print("-", i)
    print(f"Les valeurs du dictionnaire sont :")
    for i in etudiant1.values():
        print("-", i)
    print(f"Les tuplets du dictionnaire sont :")
    for i in etudiant1.items():
        print("-", i)

    etudiant2 = {
        "firstname":"lahcen",
        "name": "jaafar",
        "promo": "2025-2026",
        "group": "122"
    }

    print(f"votre nom est {etudiant2['name']}, votre prénom est {etudiant2['firstname']}, "
          f"vous faites partie de la promo {etudiant2['promo']} et votre groupe est le {etudiant2['group']}")

    print(f"Les clés du dictionnaire sont :")
    for i in etudiant2.keys():
        print("-", i)
    print(f"Les valeurs du dictionnaire sont :")
    for i in etudiant2.values():
        print("-", i)
    print(f"Les tuplets du dictionnaire sont :")
    for i in etudiant2.items():
        print("-", i)

    binome = {
        "binome1": etudiant1,
        "binome2": etudiant2
    }
    print("Les étudiants qui forment le binôme sont :")
    for i in binome:
        etudiant = binome[i]
        print(f"- L'étudiant {etudiant['name']} {etudiant['firstname']} du groupe {etudiant['group']}")
dictio()