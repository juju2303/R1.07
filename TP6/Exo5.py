def palindrome():
    import unicodedata
    import string

    def enlever_accents(txt):
        nfkd = unicodedata.normalize("NFD", txt)
        return "".join(c for c in nfkd if unicodedata.category(c) != "Mn")

    def nettoyer(txt):
        txt = txt.lower()
        txt = enlever_accents(txt)
        autorises = string.ascii_lowercase + string.digits
        return "".join(c for c in txt if c in autorises)

    def est_palindrome(txt):
        return txt == txt[::-1]

    phrase = input("Entrez un mot ou une phrase : ")
    propre = nettoyer(phrase)

    if est_palindrome(propre):
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")

palindrome()
