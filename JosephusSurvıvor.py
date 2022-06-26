def killer(size, index):
    index = index % size
    if index % size == 1:
        return index - 1
    elif index % size == 0:
        return size - 1
    else:
        return index - 1
    
    
k = 3
size = 7
liste = []
for i in range(1, size+1):
    liste.append(i)
index = k
size = len(liste)
print(liste)

while len(liste) != 1:
    index = killer(len(liste), index)
    liste.pop(index)
    print(index)
    print(liste)
    index += k
    print(index)



    