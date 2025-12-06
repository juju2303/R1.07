def monnaie():
    s = int(input("Entrez une somme en euros : "))
    r = s

    b100 = r // 100
    r = r % 100

    b50 = r // 50
    r = r % 50

    b20 = r // 20
    r = r % 20

    b10 = r // 10
    r = r % 10

    b5 = r // 5
    r = r % 5

    p2 = r // 2
    r = r % 2

    p1 = r

    print(f"{s} euros, c'est donc {b100} billets de 100, {b50} de 50, {b20} de 20, {b10} de 10, {b5} de 5, {p2} pieces de 2 et {p1} piece 1.")

monnaie()
