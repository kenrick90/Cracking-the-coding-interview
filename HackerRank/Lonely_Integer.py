# Lonely Integer
# https://www.hackerrank.com/challenges/lonely-integer/problem
def lonely_integer(a):

	table = [0] * 100

	for num in a:
		table[num] += 1

	for i in range(100):
		if table[i] == 1:
			return i


if __name__ == "__main__":
	n = int(input())

	a = list(map(int, input().rstrip().split()))

	print(lonely_integer(a))





