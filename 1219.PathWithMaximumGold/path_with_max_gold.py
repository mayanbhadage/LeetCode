class Solution:
    def __init__(self):
        self.max_gold = 0
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        #Find the cell with gold
    
        for row in range(m):
            for col in range(n):
                #This means we have found the gold at current cell
                if grid[row][col] != 0: 
                    #not we need to store that gold in a temp variable so that we 
                    #will not visit it again
                    temp = grid[row][col]
                    grid[row][col] = 0
                    self.dfs(grid,row, col, temp)
                    grid[row][col] = temp
        return self.max_gold
                    
    def dfs(self, grid, row, col, gold):
        self.max_gold = max(self.max_gold, gold)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for x, y in directions:
            nx = row + x
            ny = col + y
            if 0<= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                tmp = grid[nx][ny]
                grid[nx][ny] = 0
                self.dfs(grid, nx, ny, gold + tmp)
                grid[nx][ny] = tmp
                
        