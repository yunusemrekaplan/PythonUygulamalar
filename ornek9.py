integers = [1707123, 3871729, -792461, 7081649, -3293037, 3392817, 3411097, 294935, 3406805, 5362713, -2341237, -483481, 9687747, 725495, 8420739, -226625, 5776567, -3213815, -8288703, -4703887, -3652417, 5802471, 8937609, -7356371, 6008105, -5645393, -471547, 3838688, 6862725, 4945305]
countC = 0
countT = 0

for i in range(0,3):
    if integers[i] % 2 == 0:
        countC += 1
    else:
        countT += 1

if countC > 1:
    for i in integers:
        if i % 2 != 0:
            print(i)
elif countT > 1:
    for i in integers:
        if i % 2 == 0:
            print(i)



