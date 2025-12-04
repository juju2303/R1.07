def palindromes():
    txt = input("Entrez un mot ou une phrase : ")
    txt = txt.lower()
    clean = ""
    for c in txt:
        if c.isalpha():
            clean += c
    if clean == clean[::-1]:
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

palindromes()
