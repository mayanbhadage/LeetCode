class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        num_island = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_island += 1
                    queue = deque([(row,col)])
                    self.bfs(queue, grid)
        return num_island
                    
                    
    def bfs(self,queue, grid):
        while(queue):
            currRow, currCol = queue.popleft()
            
            for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                newRow = currRow + direction[0]
                newCol = currCol + direction[1]
                
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    if grid[newRow][newCol] == "1":
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = "-1"
        