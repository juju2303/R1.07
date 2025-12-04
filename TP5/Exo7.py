def verification():
    import os.path
    import datetime

    f1 = input("Entrez le nom du premier fichier : ")
    f2 = input("Entrez le nom du second fichier : ")

    if os.path.isfile(f1):
        print(f"Taille de {f1} :", os.path.getsize(f1), "octets")
    else:
        print(f"{f1} n'existe pas.")

    if os.path.isfile(f2):
        print(f"Taille de {f2} :", os.path.getsize(f2), "octets")
    else:
        print(f"{f2} n'existe pas.")

    if os.path.isfile(f1) and os.path.isfile(f2):
        m1 = os.path.getmtime(f1)
        m2 = os.path.getmtime(f2)

        if m1 > m2:
            print(f"{f1} est le plus recent :", datetime.datetime.fromtimestamp(m1))
        else:
            print(f"{f2} est le plus recent :", datetime.datetime.fromtimestamp(m2))

verification()
