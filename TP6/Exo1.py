def liste():
    L1 = [0]*3
    print(L1, type(L1), id(L1))

    for x in L1:
        print(x, type(x), id(x))

    L1[1] = L1[1] + 1
    print(L1, type(L1), id(L1))

    for x in L1:
        print(x, type(x), id(x))

    s = "machaine"
    print(s, id(s))
    for c in s:
        print(c, type(c), id(c))

liste()
