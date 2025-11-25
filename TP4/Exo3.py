def scalaire():
    nMax = 10
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    while n < 1 or n > nMax:
        n = int(input(f"Veuillez entrer une valeur entre 1 et {nMax} : "))

    v1 = []
    v2 = []

    print("Saisie du premier vecteur :")
    for i in range(n):
        v1.append(int(input(f"v1[{i}] = ")))

    print("Saisie du second vecteur :")
    for i in range(n):
        v2.append(int(input(f"v2[{i}] = ")))

    produit_scalaire = 0
    for i in range(n):
        produit_scalaire += v1[i] * v2[i]

    return produit_scalaire


resultat = scalaire()
print("Le produit scalaire de v1 par v2 vaut", resultat)