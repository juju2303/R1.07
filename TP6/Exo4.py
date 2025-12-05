def tableau():
    import random

    def generer(nbr, vmin, vmax):
        t = []
        for _ in range(nbr):
            t.append(random.randint(vmin, vmax))
        return t

    def combienInferieur(table, vseuil):
        c = 0
        for x in table:
            if x < vseuil:
                c += 1
        return c

    nb = int(input("Combien de valeurs generer : "))
    vmin = int(input("Valeur minimale : "))
    vmax = int(input("Valeur maximale : "))

    rep = input("Vous voulez preciser le seuil ? ").lower()
    if rep == "oui" or rep == "o":
        seuil = int(input("Quel seuil : "))
    else:
        seuil = 30

    tab = generer(nb, vmin, vmax)
    tab.sort()
    print(tab)

    total = combienInferieur(tab, seuil)
    print(f"Il y en a {total} inferieurs a {seuil}")

tableau()
