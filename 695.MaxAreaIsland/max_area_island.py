class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        if not rows:
            return max_area
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    area = self.dfs(row, col, grid, 1)
                    max_area = max(max_area, area)

        return max_area
        
    def dfs(self, row, col, grid , area):
        direction = [(-1,0), (1,0), (0,-1),(0,1)]
        for d in direction:
            newRow = row + d[0]
            newCol = col + d[1]
            
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 0
                    area = self.dfs(newRow, newCol, grid, area + 1)
        return area
                        