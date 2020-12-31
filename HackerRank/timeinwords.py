#!/bin/python3
#https://www.hackerrank.com/challenges/the-time-in-words/problem

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    unit_number = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty'}
    
    if m==0:
        return unit_number[int(h)] + " o' clock"
    if m ==1:
        return "one minute past " + unit_number[int(h)]
    if m == 15:
        return "quarter past " + unit_number[int(h)]
    if m==30:
        return "half past " + unit_number[int(h)]
    if m ==45:
        return "quarter to " + unit_number[(int(h)+1)%12]  
    if m ==59:
        return "one minute to " + unit_number[(int(h)+1)%12]
    
    if m>0 and m < 15:
        return unit_number[int(m)] + " minutes past " + unit_number[int(h)]

    if m>15 and m < 21:
        return unit_number[int(m)] + " minutes past " + unit_number[int(h)]  
    
    if m>20 and m < 30:
        return "twenty " + unit_number[int(str(m)[1])] + " minutes past " + unit_number[int(h)]    

    if m >30 and m < 40:
        return "twenty " + unit_number[int(str(60-m)[1])] + " minutes to " + unit_number[(int(h)+1)%12]
    
    if m >=40:
        return unit_number[60-m] + " minutes to " + unit_number[(int(h)+1)%12]


          
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
