string = 'Yunus emre kaplan yunus\'un'
string = string.split()

for eleman in range(0,len(string)):
    kelime = string[eleman]
    kelime = kelime.capitalize()
    string[eleman] = kelime

string = ' '.join(string)


print(string)
    
    