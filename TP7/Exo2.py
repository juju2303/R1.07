def dossier():
    import sys
    import os

    def aide():
        print("Erreur : utilisation incorrecte.")
        print("Utilisation : python find1.py <nom_dossier>")

    def affiche(dossier):
        for x in os.listdir(dossier):
            print(x)

    args = sys.argv

    if len(args) != 2:
        aide()
        return

    d = args[1]

    if not os.path.exists(d) or not os.path.isdir(d):
        print("Erreur : le dossier n'existe pas.")
        aide()
        return

    affiche(d)
