# https://www.hackerrank.com/challenges/most-commons/problem
# Company Logo
from collections import Counter

if __name__ == "__main__":
	a=list(input().rstrip())
	a.sort()
	number=0
	for key,value in Counter(a).most_common()[0:3]:
		print(key,value)



