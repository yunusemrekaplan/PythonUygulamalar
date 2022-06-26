from contextlib import AsyncContextDecorator
from turtle import clear


string = 'helloworldyunus'
let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ""
control = 0

for i in range(0, len(string)):
    for j in range(0, len(let)):
        if string[i] == let[j]:
            control = 1
            break;
    if control == 1:
        s += ' '
        s += string[i]
    else:
        s += string[i]
    control = 0




print(s)
