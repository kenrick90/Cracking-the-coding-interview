#!/bin/python3
#https://www.hackerrank.com/challenges/absolute-permutation/problem
import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    perm=[]
    for i in range(1,n+1):
        perm.append(i)
        
    if k==0:
        return perm
        
    if (n/k)%2 !=0 :
        return [-1]
        
    add = True
    counter=0

    for i in range (n):
        if add==True:
            perm[i] += k
        else:
            perm[i] -= k

        counter += 1
        if counter == k and add == True:
            add = False
            counter = 0
        if counter == k and add == False:
            add = True
            counter = 0

        
            
    return perm
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
