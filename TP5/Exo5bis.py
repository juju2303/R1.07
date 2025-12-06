def FicheDePaye():
    h = float(input("Entrez le nombre d'heures travaillées (hors jours fériés, dimanche compris) ce mois-ci : "))
    s = float(input("Entrez le salaire horaire : "))
    jour_f = float(input("Entrez le nombre total d'heures travaillées les jours fériés (dimanche inclus) ce mois-ci : "))


    if h <= 151.67:
        salaire = h * s + jour_f * (s * 2)
    else:
        salaire = 151.67 * s + (h - 151.67) * (s * 1.25) + jour_f * (s * 2)

    print(f"Le salaire est de : {salaire} €")

FicheDePaye()
