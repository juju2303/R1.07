from random import randint


def nb_mystere():
    x = randint(0, 100)
    compteur = 0
    while True:
        n = int(input("Votre proposition : "))
        compteur += 1
        if n < x:
            print("Le nombre est plus grand !")
        elif n > x:
            print("Le nombre est plus petit !")
        else:
            print(f"Bravo vous avez trouvez le nombre {x} en {compteur} tentatives !")
print(nb_mystere())
nb_mystere()