def reference():
    def ajouter_elt(lst=[0,1,2], elt=3):
        lst.append(elt)
        print(lst, id(lst))
        return lst

    print(ajouter_elt())
    print(ajouter_elt())

    def ajouter_carac(ch="abc", elt="d"):
        print(ch, id(ch))
        print(elt, id(elt))
        return ch + elt

    print(ajouter_carac())
    print(ajouter_carac())

reference()
