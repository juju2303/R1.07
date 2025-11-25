import time


def factoriel():
    n = int(input("Entrer l'entier dont vous voulez connaître le factoriel : "))
    choix = input("Tapez 'for' pour boucle for ou 'while' pour boucle while : ")
    start = time.time()
    if choix == "for":
        fact = 1
        for i in range(1, n + 1):
            fact *= i
            print(f"Etapes = {i} : Factoriel = {fact}")
    elif choix == "while":
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            print(f"Etapes = {i} : Factoriel = {fact}")
            i += 1
    else:
        print("Choix non reconnu.")
    end = time.time()
    print(f"Temps d'exécution : {end - start} secondes.")
factoriel()
