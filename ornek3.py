s = "aaaxbbbbyyhwawiwjjjwwm"
pay = 0
payda = len(s)

for i in range(0, len(s)):
    if (s[i] == 'a') or (s[i] == 'b') or (s[i] == 'c') or (s[i] == 'd') or (s[i] == 'e') or (s[i] == 'f') or (s[i] == 'g') or (s[i] == 'h') or (s[i] == 'i') or (s[i] == 'j') or (s[i] == 'k') or (s[i] == 'l') or (s[i] == 'm'):
        continue
    else:
        pay += 1

print('{} / {}'.format(pay, payda))
