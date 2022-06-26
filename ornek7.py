s = 'man i need a taxi up to ubud'
s = s.upper()
s = s.split()
let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
point = 0
i = 0
liste = []

while i < len(s):
    j = 0
    while j < len(s[i]):
        temp = s[i]
        k = 0
        while k < len(let):
            if temp[j] == let[k]:
                point += k + 1
                break
            k += 1
        j += 1
                
    liste.append(point)
    i += 1
    point = 0

temp = max(liste)
temp = liste.index(temp)
temp = s[temp]
temp = temp.lower()
print(temp)
