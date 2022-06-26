def climbingLeaderboard(ranked, player):
    size = len(player)
    counter = 0
    while(counter < size):
        rank = 1
        sira = {}
        playerSira = []
        #for i in player:
        rankedN = []
        rankedN = ranked
        point = player[counter]
        rankedN.append(point)
        rankedN.sort()
        for j in range(0, len(rankedN)):
            if rankedN[j] != rankedN[j-1]:
                sira.append(rank)
                rank += 1
        for j in range(0, len(rankedN)):
            if rankedN[j] == point:
                temp = sira[j]
                playerSira.append(temp)
        #ranked.remove(i)
        counter += 1    
        
    return playerSira

ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]


print(climbingLeaderboard(ranked, player))