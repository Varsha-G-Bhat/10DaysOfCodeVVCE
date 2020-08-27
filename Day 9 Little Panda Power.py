import os
import sys

def gcd(a,b):
    if b == 0:
        return (1,0)
    else:
        x, y = gcd(b, a % b)
        return(y, x - (a // b) * y)

def modInverse(a, x):
    y, m = gcd(a, x)
    return(x + y % x) % x

def solve(a, b, x):
    if b > 0:
        return pow(a,b,x)
    else:
        return int(pow(modInverse(a, x), -b, x))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = solve(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()