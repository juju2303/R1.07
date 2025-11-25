def location():
    while True:
        h = int(input("Donnez l'heure de début de la location (un entier) : "))
        H = int(input("Donnez l'heure de fin de la location (un entier) : "))
        if h > H:
            print("Attention ! l'heure de début de la location est après la fin de la location !")
            continue
        elif h == H:
            print("Attention ! l'heure de début de la location est la même que l'heure de fin de la location !")
            continue
        elif h < 0 or h > 24 or H < 0 or H > 24:
            print("Les heures doivent être comprises entre 0 et 24 !")
            continue
        else:
            break

    if h > 7 and H <= 17:
        print("Vous avez loué votre vélo pendant : ")
        print(H - h, "heures au tarif de 2 euro(s)")
        print("Le montant total à payer est de", 2*(H - h), "€.")
location()