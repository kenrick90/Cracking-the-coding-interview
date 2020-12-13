# https://www.hackerrank.com/challenges/equal/problem

def minOperationEqual(arr,n):
	Equal = False

	maximum = arr[0]
	minimum = arr[0]
	for i in range(n):
		if arr[i] > maximum:
			maxIndex = i
			maximum = arr[i]
		if arr[i] < minimum:
			minIndex = i
			minimum = arr[i]


if __name__ == "__main__":
	t = int(input())
	n = int(input())
	arr = list(map(int,input().rstrip().split()))
	return minOperationEqual(arr,n)