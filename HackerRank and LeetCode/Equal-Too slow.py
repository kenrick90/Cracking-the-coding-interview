# https://www.hackerrank.com/challenges/equal/problem

def determineOperation(diff):
	if diff >= 5:
		return 5
	if diff >= 2:
		return 2
	return 1

def minOperationEqual(arr,n):
	arr.sort(reverse=True)
	operation = 0
	while arr[0] != arr[n-1]:
		operation += 1
		arr[0] -= determineOperation(arr[0]-arr[n-1])
		arr.sort(reverse=True)
	return operation

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int,input().rstrip().split()))
		print(minOperationEqual(arr,n))