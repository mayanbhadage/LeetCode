class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        grid[0][0] = 1
        min_steps = math.inf
        #self.dfs(0,0,grid,1)
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)]
        queue = deque([(0,0,1)])
        seen = set()
        while queue:
            num_neighbours = len(queue)
            
            for _ in range(num_neighbours):
                currRow, currCol, steps = queue.popleft()
                
                if currRow == N-1 and currCol == N-1:
                    min_steps = min(steps, min_steps)
                else:
                    if steps < min_steps:
                        for d in directions:
                            newRow = currRow + d[0]
                            newCol = currCol + d[1]

                            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                                if grid[newRow][newCol] == 0:
                                    grid[newRow][newCol] = 1
                                    queue.append((newRow,newCol,steps+1))

                            
                    
        if min_steps == math.inf:
            return -1
        return min_steps
        
        
        
    def dfs(self,currRow, currCol, grid, steps):
        if currRow == len(grid) - 1 and currCol == len(grid) - 1:
            self.min_steps = min(self.min_steps, steps)
            return
        
        
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)]
        if steps < self.min_steps:
            for d in directions:
                newRow = currRow + d[0]
                newCol = currCol + d[1]

                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    if grid[newRow][newCol] == 0:
                        grid[newRow][newCol] = 1
                        self.dfs(newRow, newCol, grid ,steps + 1)
                        grid[newRow][newCol] = 0
