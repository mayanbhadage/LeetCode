class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Calculate Number Of Rotten Oranges
        
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        fresh = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        if len(rotten) == 0:
            if fresh > 0:
                return -1
            else:
                return 0
        time = 0
        while rotten and fresh > 0:
            time += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for direction in directions:
                    nx = x + direction[0]
                    ny = y + direction[1]
                    
                    
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        if grid[nx][ny] == 1:
                            fresh -= 1
                            grid[nx][ny] = 2
                            rotten.append((nx,ny))
        
        if fresh > 0:
            return -1 
        else:
            return time