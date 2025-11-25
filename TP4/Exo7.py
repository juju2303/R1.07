def tuplets():
    binome = ("login1", "login2")
    print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")

    nouveau_login = input("Entrez le nouveau login pour le second membre du binome : ")
    try:
        binome[1] = nouveau_login
    except TypeError:
        print("Erreur : les tuples sont immuables, on ne peut pas modifier un élément directement.")

    try:
        del binome[1]
    except TypeError:
        print("Erreur : on ne peut pas supprimer un élément individuel d’un tuple.")

    trinome = binome + ("login3",)
    print("Nouveau trinome :", trinome)

    return binome, trinome

tuplets()
