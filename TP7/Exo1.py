def argument():
    import sys

    args = sys.argv
    nb = len(args)

    if nb == 1:
        print(f"Pas assez d'arguments pour le script '{args[0]}'")
    else:
        for i in range(1, nb):
            print(args[i])

argument()
