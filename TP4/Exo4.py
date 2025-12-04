'''
def liste():
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

    max_freq = 0
    max_elem = None

    for elem in L1:
        freq = 0
        for e in L1:
            if e == elem:
                freq += 1

        # On garde le premier élément rencontré qui a la fréquence max
        if freq > max_freq:
            max_freq = freq
            max_elem = elem

    return max_elem, max_freq


# Programme principal
nombre, frequence = liste()
print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({frequence} x)")
'''

def liste():
    L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

    max_freq = 0
    max_elem = None

    for elem in L1:
        freq = L1.count(elem)

        if freq > max_freq:
            max_freq = freq
            max_elem = elem

    return max_elem, max_freq


# Programme principal
nombre, frequence = liste()
print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({frequence} x)")
