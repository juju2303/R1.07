def FicheDePaye():
    h = float(input("Entrez le nombre d'heures travaillees : "))
    s = float(input("Entrez le salaire horaire : "))

    if h <= 160:
        salaire = h * s
    elif h <= 200:
        salaire = 160 * s + (h - 160) * (s * 1.25)
    else:
        salaire = 160 * s + 40 * (s * 1.25) + (h - 200) * (s * 1.50)

    print("Le salaire est :", salaire)

FicheDePaye()
