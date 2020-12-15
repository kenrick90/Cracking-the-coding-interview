# https://www.hackerrank.com/challenges/equal/problem

memo={}

def determineOperations(diff):
	if diff in memo:
		return memo[diff]
	operation=0
	operation += diff // 5
	remainder = diff % 5
	operation += remainder // 2
	remainder = remainder % 2
	operation += remainder
	memo[diff] = operation
	return operation

def numberOfOperations(arr, n, minimum):
	operations = 0
	for i in range(n):
		operations += determineOperations(arr[i]-minimum)
	return operations

def minOperationEqual(arr,n):
	arr.sort(reverse=True)
	operation = 0
	min1 = arr[n-1]
	min2 = min1 - 1
	min3 = min2 - 1
	min4 = min3 - 1
	min5 = min4 - 1
	return min(numberOfOperations(arr,n,min1), numberOfOperations(arr,n,min2), numberOfOperations(arr,n,min3), numberOfOperations(arr,n,min4), numberOfOperations(arr,n,min5))


if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int,input().rstrip().split()))
		print(minOperationEqual(arr,n))