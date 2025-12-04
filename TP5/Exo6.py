def string():
    T = input("Entrez une chaine : ")

    # 1. Taille de la chaine
    taille = 0
    for c in T:
        taille += 1

    print("Taille de la chaine :", taille)

    # 2. Pourcentage de voyelles
    voyelles = "aeiouyAEIOUY"
    nb_voyelles = 0
    for c in T:
        for v in voyelles:
            if c == v:
                nb_voyelles += 1
                break

    if taille > 0:
        pourcentage = (nb_voyelles * 100) / taille
    else:
        pourcentage = 0

    print("Pourcentage de voyelles :", pourcentage)

    # 3. Tester si 'wagon' est une sous-chaine
    motif = "wagon"
    long = 0
    for c in motif:
        long += 1

    pos = -1
    for i in range(taille - long + 1):
        ok = True
        for j in range(long):
            if T[i + j].lower() != motif[j]:
                ok = False
                break
        if ok:
            pos = i
            break

    if pos != -1:
        print("La chaine 'wagon' existe, premiere occurrence a :", pos)
    else:
        print("La chaine 'wagon' n'existe pas")

    # 4. Nombre d'occurrences de 'wagon'
    occ = 0
    for i in range(taille - long + 1):
        ok = True
        for j in range(long):
            if T[i + j].lower() != motif[j]:
                ok = False
                break
        if ok:
            occ += 1

    print("Nombre d'occurrences de 'wagon' :", occ)

string()
