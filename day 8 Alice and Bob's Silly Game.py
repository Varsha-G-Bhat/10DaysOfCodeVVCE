import os
import sys

primeNumbers = [2]
def isPrime(num):
    for i in range(2,int((num)**0.5)+1):
        if num % i == 0:
            return False
    return True

def sillyGame(n):
    LargestPrime = primeNumbers [-1]
    if n > LargestPrime :
        for i in range(LargestPrime + 1,n+1):
            if isPrime(i):
                primeNumbers.append(i)
    return "Alice" if sum(i <= n for i in primeNumbers) % 2 else 'Bob'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()