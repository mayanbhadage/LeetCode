class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        
        
        num_island = 0
        temp = []
        for row in range(rows):
            for col in range(cols):
                string = []
                if grid[row][col] == 1:
                    string.append("S")
                    grid[row][col] = 0
                    num_island += 1
                    self.dfs(row, col, grid, string)
                    temp.append(string)
        x = set()
        for t in temp:
            x.add(tuple(t))
        return len(x)
        
    def dfs(self, currRow, currCol, grid, string):
        
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            newRow = currRow + d[0]
            newCol = currCol + d[1]
            
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 0
                    if d == (-1,0):
                        string.append("U")
                    elif d == (1,0):
                        string.append("D")
                    elif d == (0,-1):
                        string.append("L")
                    else:
                        string.append("R")
                    self.dfs(newRow, newCol, grid, string)
            
                
        string.append("X")