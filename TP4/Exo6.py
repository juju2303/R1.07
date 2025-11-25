def tri():
    tab = [5, 2, 4, 8, 1, 3]

    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        if min_index != i:
            tab[i], tab[min_index] = tab[min_index], tab[i]
        print(tab)

    return tab

liste_triee = tri()

# Partie 2
tab = [5, 2, 4, 8, 1, 3]
print("sorted(tab) =", sorted(tab))
print("tab après sorted(tab) =", tab)

# Partie 3
tab.sort()
print("tab après tab.sort() =", tab)
