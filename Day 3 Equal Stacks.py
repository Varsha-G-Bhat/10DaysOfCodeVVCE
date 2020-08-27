import os
import sys

def equalStacks(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    n1=0
    n2=0
    n3=0
    minsum = min(sum1, sum2, sum3)
    while(True):
        if sum1 == 0 or sum2 == 0 or sum3 == 0 :
            return 0
        elif sum1 == sum2 == sum3:
            return sum1 
        elif sum1 > minsum :
            sum1 = sum1 - h1[n1]
            n1 = n1 + 1
        elif sum2 > minsum :  
            sum2 = sum2 - h2[n2]
            n2 = n2 + 1
        elif sum3 > minsum :
            sum3 = sum3 - h3[n3]
            n3 = n3 + 1
        minsum = min(sum1, sum2, sum3)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N1N2N3 = input().split()

    n1 = int(N1N2N3[0])

    n2 = int(N1N2N3[1])

    n3 = int(N1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
