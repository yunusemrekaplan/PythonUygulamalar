string = input()
countX = 0
countO = 0

for i in range(0, len(string)):
    if (string[i] == 'X') or (string[i] == 'x'):
        countX += 1
    elif (string[i] == 'O') or (string[i] == 'o'):
        countO += 1
    
if countX == countO:
    print('True')
else: 
    print('False')