import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    answer = a[d:] + a[:d]
    fptr.write(' '.join(map(str, answer)))
    fptr.close()
