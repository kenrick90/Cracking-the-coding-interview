class Solution:
    def countSubstrings(self, s: str) -> int:
    	lenS = len(s)
    	matrix = [[None for i in range(lenS)] for j in range(lenS) ]
    	# print(matrix)
    	count =0

    	# 1 represents a palindome, since matrix[1][1] represents 1 character, its a palindome
    	for i in range(lenS):
    		matrix[i][i] = 1
    		count+=1
    		# print(matrix)

    	#looping through 2 characters 
    	for i in range(lenS-1):
    		if s[i] == s[i+1]:
    			matrix[i][i+1]=1
    			count+=1
    		else:
    			matrix[i][i+1]=0
    	
    	#loop for 3 or more characters
    	for i in range(2,lenS):
    		runner = i
    		row=0
    		while runner != lenS:
    			if matrix[row+1][runner-1] == 1 and s[row] == s[runner]:
    				matrix[row][runner] = 1
    				count +=1
    			else:
    				matrix[row][runner] = 0
    			runner+=1
    			row+=1

    	# print(matrix)
    	return count

if __name__ == "__main__":
	sol = Solution()
	# print(sol.countSubstrings("a")

	assert sol.countSubstrings("aabaca") == 9 ,"wrong"
	assert sol.countSubstrings("abc") == 3 ,"wrong"
