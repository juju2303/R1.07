def liste():
    def ajouter_elt(lst, elt):
        lst.append(elt)
        return lst

    lst1 = [0, 1, 2]
    lst2 = ajouter_elt(lst1, len(lst1))

    print(lst1, id(lst1))
    for x in lst1:
        print(x, id(x))

    print(lst2, id(lst2))
    for x in lst2:
        print(x, id(x))

liste()
