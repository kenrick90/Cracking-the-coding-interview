# https://www.hackerrank.com/challenges/equal/problem

def determineOperation(diff):
	if diff >= 5:
		return 5
	if diff >= 2:
		return 2
	return 1

def minOperationEqual(arr,n):
	secondMaximum = maximum = minimum = arr[0]
	secondmaxIndex = maxIndex = minIndex = 0

	for i in range(n):
		if arr[i] > maximum:
			secondmaxIndex = maxIndex
			secondMaximum = maximum
			maxIndex = i
			maximum = arr[i]
			continue

		if arr[i] > secondMaximum:
			secondmaxIndex = i
			secondMaximum = arr[i]
			continue

		if arr[i] < minimum:
			minIndex = i
			minimum = arr[i]
			continue

	operation = 0
	#maximum = 3 maxIndex = 2
	#minimum = 2 minIndex = 0
	#operation = 1
	# print(maximum,secondMaximum,minimum)

	while maximum != minimum:

		# print(maximum,maxIndex)
		arr[maxIndex] -= determineOperation(maximum - minimum)
		operation += 1
		#case 1
		if arr[maxIndex] < secondMaximum:
			prevSecondMaxIndex = secondmaxIndex
			prevSecondMaximum = secondMaximum
			secondmaxIndex = maxIndex
			secondMaximum = arr[maxIndex]
			maxIndex = prevSecondMaxIndex
			maximum = prevSecondMaximum
		else:
			maximum = arr[maxIndex]
	return operation


if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int,input().rstrip().split()))
		print(minOperationEqual(arr,n))