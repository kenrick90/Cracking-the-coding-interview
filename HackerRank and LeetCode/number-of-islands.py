#https://leetcode.com/problems/number-of-islands/submissions/
class Solution:
    
    def dfs(self,grid: List[List[str]],row,col):
        if row == -1 or col == -1 or row == len(grid) or col == len(grid[0]) or grid[row][col] != "1":
            return
        grid[row][col] = "#"
        self.dfs(grid,row - 1,col)
        self.dfs(grid,row + 1,col)
        self.dfs(grid,row,col - 1)
        self.dfs(grid,row,col + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        numisland=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    numisland+=1
                    self.dfs(grid,row,col)
        # print(newgrid)
        return numisland
