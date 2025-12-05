def find():
    import sys
    import os

    def recherche(dossier):
        listeFichiers = []
        listeDossiers = []

        liste = os.listdir(dossier)
        for elt in liste:
            chemin = dossier + "/" + elt
            if os.path.isfile(chemin):
                listeFichiers.append(chemin)
            elif os.path.isdir(chemin):
                listeDossiers.append(chemin)

        i = 0
        while i < len(listeDossiers):
            sous = listeDossiers[i]
            contenu = os.listdir(sous)
            for elt in contenu:
                chemin2 = sous + "/" + elt
                if os.path.isfile(chemin2):
                    listeFichiers.append(chemin2)
                elif os.path.isdir(chemin2):
                    listeDossiers.append(chemin2)
            i += 1

        return listeFichiers, listeDossiers

    if len(sys.argv) != 2:
        print("Utilisation : python find2.py <dossier>")
        return

    dossier = sys.argv[1]

    if not os.path.exists(dossier) or not os.path.isdir(dossier):
        print("Erreur : dossier invalide.")
        return

    fichiers, dossiers = recherche(dossier)

    print("FICHIERS :")
    for f in fichiers:
        print(f)

    print("DOSSIERS :")
    for d in dossiers:
        print(d)
