# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether
# any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def AnyTwoNumber(listOfNumber,k):
	numbermap = [0] * (k+1)

	for number in listOfNumber:
		numbermap[number] += 1

	i , j = 0 , k

	while i <= j:
		if i == j and numbermap[i]>=2:
			return True

		if numbermap[i] > 0 and numbermap[j] > 0:
			return True
		i +=1
		j -=1

	return False
	numbermap = [0] * (k+1)

	for number in listOfNumber:
		numbermap[number] += 1

	i , j = 0 , k

	while i != j:
		if numbermap[i] > 0 and numbermap[j] > 0:
			return True
			
if __name__ == '__main__':
	assert AnyTwoNumber([10,15,3,0,1,1,1,1,1,7],17) == True, "Should be True"

