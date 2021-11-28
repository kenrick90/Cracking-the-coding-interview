#https://leetcode.com/problems/pascals-triangle/submissions/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [ None for _ in range(numRows)]

        for i in range(1, numRows+1):
            output[i-1] = [1 for _ in range(i)]

        for i in range(2,numRows,1):
            for j in range(1,i,1):
                output[i][j] = output[i-1][j-1] + output[i-1][j]
        return output
        
