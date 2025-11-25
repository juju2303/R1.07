def VerificationDate():
    date_str = input("Entrez une date au format jjmmaaaa : ")

    if len(date_str) != 8 or not date_str.isdigit():
        print("Format incorrect, veuillez saisir une date en jjmmaaaa.")
        return False

    jj = int(date_str[0:2])
    mm = int(date_str[2:4])
    aaaa = int(date_str[4:8])

    def bissextile(annee):
        return (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0)

    if mm < 1 or mm > 12:
        print("Mois incorrect : doit être entre 1 et 12.")
        return False

    if mm in [1,3,5,7,8,10,12]:
        max_jours = 31
    elif mm in [4,6,9,11]:
        max_jours = 30
    else:
        max_jours = 29 if bissextile(aaaa) else 28

    if jj < 1 or jj > max_jours:
        print("Jour incorrect : doit être entre 1 et", max_jours, "pour ce mois.")
        return False

    print("Date valide.")
    return True

VerificationDate()
