from unittest import result

'''
def entier():
    n=int(input("Entre un nombre souhaité : "))
    result=0
    for i in range(0, n+1):
        result += i
    return result
print(entier())
'''
'''
def attente():
    n=None
    while n !=100:
        n=int(input("Entre une valeur de n : "))
    return "La boucle s'arrête"
print(attente())
'''
'''
def lecture():
    N = 0
    u = 0
    U = 0
    compteur = 0

    while compteur < 10:
        n = int(input("Entrer votre valeur : "))
        if n < 0 or n > 20:
            print("le chiffre ne remplit pas les conditions ! Veuillez réessayer.")
        else:
            if 10 <= n < 15:
                u += 1
            elif 15 <= n < 20:
                U += 1
            else:
                N += 1
            compteur += 1

    print("Il y a", N, "valeurs strictement inférieures à 10")
    print("Il y a", u, "valeurs supérieures ou égales à 10 et strictement inférieures à 15")
    print("Il y a", U, "valeurs supérieures ou égales à 15")


lecture()
'''
'''
def grand():
    n = int(input("Entrez un nombre X supérieur à 1 : "))
    N = 0
    somme = 0
    while somme <= n:
        N += 1
        somme += N
    print(N - 1)
grand()
'''