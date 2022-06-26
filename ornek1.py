string = 'ATCG'
cikti = ''


for i in range(0,len(string)):
    if string[i] == 'A':
        cikti += 'T'
    elif string[i] == 'T':
        cikti += 'A'
    elif string[i] == 'G':
        cikti += 'C'
    else: 
        cikti += 'G'


print(cikti)
    
    