def etudiant():
    nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
    moyenne = 0.0
    notes = []

    for i in range(nombreEtudiants):
        note = float(input("Note etudiant " + str(i) + " : "))

        while note < 0 or note > 20:
            note = float(input("Note etudiant " + str(i) + " (entre 0 et 20) : "))

        notes.append(note)
        moyenne = moyenne + note

    moyenne = moyenne / nombreEtudiants
    return nombreEtudiants, notes, moyenne


nb, notes, moyenne = etudiant()

print("Moyenne de classe :", moyenne)
print("Numero de l'Etudiant | note | ecart a la moyenne")

for i in range(nb):
    ecart = notes[i] - moyenne
    print(i, "|", notes[i], "|", ecart)
