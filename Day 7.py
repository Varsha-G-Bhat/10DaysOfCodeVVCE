import math
import os
import random
import re
import sys

def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    arr.sort(key = lambda num : int(num[0]))
    for i in arr:
        print(i[1], end = " ") 

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)