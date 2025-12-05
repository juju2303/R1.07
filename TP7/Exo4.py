def findfinal():
    import sys
    import os

    def recherche(dossier, fichier):
        listeFichiers = []
        listeDossiers = []

        liste = os.listdir(dossier)
        for elt in liste:
            chemin = dossier + "/" + elt
            if os.path.isfile(chemin):
                if elt == fichier:
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
                    if elt == fichier:
                        listeFichiers.append(chemin2)
                elif os.path.isdir(chemin2):
                    listeDossiers.append(chemin2)
            i += 1

        return listeFichiers, listeDossiers

    if len(sys.argv) != 5:
        print("Utilisation : python find.py -d <dossier> -f <fichier>")
        return

    try:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
    except ValueError:
        print("Arguments manquants. Utilisation : python find.py -d <dossier> -f <fichier>")
        return

    dossier = sys.argv[d_index + 1]
    fichier = sys.argv[f_index + 1]

    if not os.path.exists(dossier) or not os.path.isdir(dossier):
        print("Erreur : dossier invalide.")
        return

    fichiersTrouves, dossiersTrouves = recherche(dossier, fichier)

    for f in fichiersTrouves:
        print(f)
