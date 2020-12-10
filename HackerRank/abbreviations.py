#https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

def removeLeftMostLowerCase(a):
	a = [ _ for _ in a ]

	index = 0
	for letter in a:
		if letter.islower():
			a.pop(index)
			break
		index += 1
	a = "".join(a)
	return a

def capitaliseLeftMostLowerCase(a):
	a = [ _ for _ in a ]

	index = 0
	for letter in a:
		if letter.islower():
			a[index] = a[index].capitalize()
			break
		index += 1

	a = "".join(a)
	return a

def abbreviationRecursive(a,b):
	if a == b:
		return True
	if len(a) < len(b):
		return False
	if a.isupper() and a != b:
		return False

	if a in memo:
		return memo[a]

	memo[a] = abbreviation(removeLeftMostLowerCase(a),b) or abbreviation(capitaliseLeftMostLowerCase(a),b)
	return memo[a]


#dynamic programming

def abbreviation(a,b):
    alen = len(a)
    blen = len(b)

    dp =[[False] * (alen+1) for _ in range(blen+1) ]

    dp[0][0] = True

    for i in range(1,alen+1):
        if a[i-1].islower():
            dp[0][i] = dp[0][i-1]

    for i in range(1,blen+1):
        for j in range(1,alen+1):
            if a[j-1].isupper() and a[j-1] == b[i-1]:
                dp[i][j] = dp[i-1][j-1]

            if a[j-1].islower() and a[j-1].capitalize() == b[i-1]:
                dp[i][j] = dp[i-1][j-1] or dp[i][j-1]

            if a[j-1].islower() and a[j-1].capitalize() != b[i-1]:
                dp[i][j] = dp[i][j-1]

    return dp[blen][alen]

if __name__ == "__main__":
    numberOfQuery = int(input())

    for i in range(numberOfQuery):
        a = input()
        b = input()
        #memo = {}
        result = abbreviation(a,b)

        if result == True:
            print("YES")
        else:
            print("NO")