def multiple(num):
    mult = 1
    while num > 0:
        temp = num % 10
        num = num // 10
        mult *= temp
    return mult

num = int(input())
if num < 10:
    print(0)
    
count = 1
prod = multiple(num)
while prod > 9:
    count += 1
    prod = multiple(prod)
    

print(count)
    
    
    