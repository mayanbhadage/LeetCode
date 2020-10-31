class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        num_island = 0
        rows = len(grid)
        if not rows:
            return num_island
        cols = len(grid[0])
        
        water = 1
        land = 0
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == land:
                    self.boundry = False
                    grid[row][col] = water
                    self.dfs(row, col, grid)
                    if not self.boundry:
                        num_island += 1
        return num_island
    
    def dfs(self, row, col, grid):
        direction = [(-1,0), (1,0), (0,-1), (0, 1)]
        water = 1
        land = 0
        
        if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
            self.boundry = True
        
        for d in direction:
            newRow = row + d[0]
            newCol = col + d[1]
            
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                if grid[newRow][newCol] == land:
                    grid[newRow][newCol] = water
                    self.dfs(newRow,newCol, grid)
            
        