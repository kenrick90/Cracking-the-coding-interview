#https://www.hackerrank.com/challenges/non-divisible-subset/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    
    n = len(s)
    subset=0
    remainderCount = [0] * k
    
    #Calculate the remainder of every value in s
    for i in range(n):
        remainderCount[s[i]%k] += 1
    
    #Account for special case of numbers in s that do no have remainder, s[i]%k = 0
    #there can only be at most 1 of this special case in the subset
    if remainderCount[0] > 1:
        remainderCount[0] = 1
    
    subset += remainderCount[0]
    
    
    for i in range(1,math.floor(k/2)+1):
        if i == k-i:
            if remainderCount[i] >= 1:
                subset += 1
            continue
    # add the higher number for example if k = 3, 
        if remainderCount[i] > remainderCount[k-i]:
            subset += remainderCount[i]
        else:
            subset += remainderCount[k-i]
            continue
    
    return subset
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
