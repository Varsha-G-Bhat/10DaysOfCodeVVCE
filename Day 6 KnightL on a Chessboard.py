import math
import os
import random
import re
import sys
from collections import deque

class Point():
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count


def checkBound(curP, a, b, n, check, myQ):
    X, Y = curP.x, curP.y

    if (X - a) >= 0:
        if (Y - b) >= 0 and check[X-a][Y-b] == 0:
            myQ.append(Point(X-a, Y-b, curP.count+1))
            check[X-a][Y-b] = 1
        if (Y + b) < n and check[X-a][Y+b] == 0:
            myQ.append(Point(X-a, Y+b, curP.count+1))
            check[X-a][Y+b] = 1
    if (X + a) < n:
        if (Y - b) >= 0 and check[X+a][Y-b] == 0:
            myQ.append(Point(X+a, Y-b, curP.count+1))
            check[X+a][Y-b] = 1
        if (Y + b) < n and check[X+a][Y+b] == 0:
            myQ.append(Point(X+a, Y+b, curP.count+1))
            check[X+a][Y+b] = 1
            if (X + a) == n-1 and (Y + b) == n-1:
                return curP.count + 1   ##Check for the target point
    return -1


def step(n, a, b):
    myQ = deque()
    check = [[0]*n for i in range(n)]  ##Check whether this point is visited or not

    start = Point(0, 0, 0)
    check[start.x][start.y] = 1
    myQ.append(start)

    while len(myQ) > 0:
        curP = myQ.popleft()
        count1 = checkBound(curP, a, b, n, check, myQ)
        count2 = checkBound(curP, b, a, n, check, myQ)
        if count1 > 0 or count2 > 0: 
            return max(count1, count2)

    return -1



def knightlOnAChessboard(n):
    res = [[0]*(n-1) for i in range(n-1)]
    for i in range(n-1):
        for j in range(i, n-1):
            res[i][j] = step(n, i+1, j+1)

    for i in range(1, n-1):
        for j in range(i):
            res[i][j] = res[j][i]

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
