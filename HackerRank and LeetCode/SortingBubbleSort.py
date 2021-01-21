# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
# Sorting:Bubble Sort


def swap(j,k,a):
	temp = a[j]
	a[j] = a[k]
	a[k] = temp

def BubbleSort(a,n):
	global numberofswaps
	for i in range(n):
		for j in range(n-1):
			if a[j] > a[j+1]:
				numberofswaps +=1
				swap(j,j+1,a)

if __name__ == "__main__":
	numberofswaps = 0
	n = int(input())
	a = list(map(int,input().rstrip().split()))
	BubbleSort(a,n)
	print("Array is sorted in {} swaps.".format(numberofswaps))
	print("First Element: {}".format(a[0]))
	print("Last Element: {}".format(a[n-1]))

