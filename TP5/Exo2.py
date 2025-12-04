def notes():
    notes = []
    coeffs = []
    for i in range(5):
        saisie = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
        s = saisie.split(" ")
        notes.append(float(s[0]))
        coeffs.append(int(s[1]))

    total = 0
    coef_total = 0
    for i in range(5):
        total += notes[i] * coeffs[i]
        coef_total += coeffs[i]

    moyenne = total / coef_total

    print("Moyenne generale :", moyenne)

    if moyenne > 10 and min(notes) >= 8:
        print("Etudiant admis")
    else:
        print("Etudiant non admis")

notes()
