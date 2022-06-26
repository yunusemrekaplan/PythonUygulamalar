word = "stress"

wordL = word.lower()
liste = []
control = 1
outListe = []

for i in range(0, len(word)):
    for j in range(i + 1, len(word)):
        if wordL[i] == wordL[j]:
            control = 0
            temp = wordL[i]
            liste.append(temp)
            break
        for k in range(0, len(liste)):
            if wordL[i] == liste[k]:
                control = 0
                break
    if control == 1:
        outListe.append(word[i])
    control = 1


print(outListe)