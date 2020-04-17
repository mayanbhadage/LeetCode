class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS solution
        
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        num_island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_island += 1
                    self.dfs(row,col,grid)
        return num_island
        
    def dfs(self, row,col, grid):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] == "1":
                grid[row][col] = "-1"
            
                self.dfs(row + 1, col, grid)
                self.dfs(row - 1, col, grid)
                self.dfs(row , col + 1, grid)
                self.dfs(row, col - 1, grid)
        