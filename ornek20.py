s1 = 'sdsziwzxdfkhqo'
s2 = 'aqkswofdizdhzsx'
s2 = list(s2)
ss1 = list(s1)

for i in range(0, len(s2)):
    temp = s2[i]
    count2 = s2.count(temp) 
    count1 = ss1.count(temp)
    if count1 != count2:
        print(False)
    if s1.find(temp) == -1:
        print(False)
        break


print(True)





