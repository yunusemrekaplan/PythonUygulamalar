arr = [27, 67, 80, 38, 21]
guide = [2, 5, 3, 1, 4]
myAr = arr

for i in range(0, len(guide)):
    if guide[i] == -1:
        continue
    else:
        for j in range(i, len(guide)):
            for k in range(j, len(guide)):
                if guide[j] == -1:
                    continue
                elif guide[i] > guide[k]:
                    temp = guide[i]
                    guide[i] = guide[k]
                    guide[k] = temp
                    temp = myAr[i]
                    myAr[i] = myAr[k]
                    myAr[k] = temp
                    print(myAr)
                    print(guide)
                    break
            

print(arr)




