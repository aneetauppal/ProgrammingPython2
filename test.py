#!/usr/bin/python
R=3
C=3

def minPath(cost, x, y):
    mincost = [[0 for x in range(C)] for x in range(R)]
    mincost[0][0] = cost[0][0]

    for i in range(1, x + 1):
        mincost[i][0] = mincost[i-1][0]+cost[i][0] 
    for j in range(1, y+1):
        mincost[0][j] = mincost[0][j-1]+cost[0][j]
    for i in range(1, y+1):
        for j in range(1, x+1):
            mincost[i][j] = min(mincost[i-1][j-1], mincost[i-1][j],
                                mincost[i][j-1] + cost[i][j])
    return mincost[x][y]


#inputList =[[i+j for i in range(10)] for j in range(10)]
cost=[[1,2,3],[4,8,2],[1,5,3]]

print (minPath(cost, 2,2))
