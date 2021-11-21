
#https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        #m is height
        m = len(grid)
        
        #n is length
        n = len(grid[0])
        
        spg = [[None for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    spg[i][j] = grid[i][j]
                
                elif i == 0:
                    spg[i][j] = grid[i][j] + spg[i][j-1]
                
                elif j == 0:
                    spg[i][j] = grid[i][j] + spg[i-1][j]
                    
                else:
                    spg[i][j] = grid[i][j] + min(spg[i-1][j], spg[i][j-1])
        
        
        return spg[m-1][n-1]
