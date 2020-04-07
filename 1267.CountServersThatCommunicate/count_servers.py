class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 0 or cols == 0:
            return 0
            
        
        points = []
        connected = 0
        
        connection_row = [0] * rows
        connection_col = [0] * cols
        
        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == 1:
                    points.append((row,col))
                    connection_row[row] += 1
                    connection_col[col] += 1
        
        for point in points:
            x,y = point
            
            if connection_row[x] > 1 or connection_col[y] > 1:
                
                connected += 1
        
        return connected