def multiplication(x):
    resultats = []
    for i in range(10):
        resultats.append(round(x * i, 1))
    return resultats

# programme principal
x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

table = multiplication(x)

for i in range(10):
    print(x, "*", i, "=", table[i])
