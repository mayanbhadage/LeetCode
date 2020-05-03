class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        
        queue = deque([start])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        maze[start[0]][start[1]] = -1
        
        while queue:
            currRow, currCol = queue.popleft()
            
            if currRow == destination[0] and currCol == destination[1]:
                return True
            
            for d in directions:
                newRow = currRow + d[0]
                newCol = currCol + d[1]
                
                
                while(0<= newRow< rows and 0<=newCol<cols and maze[newRow][newCol] !=1):
                    newRow += d[0]
                    newCol += d[1]
                    
                newRow -=d[0]
                newCol -= d[1]
                
                if maze[newRow][newCol] == 0:
                    maze[newRow][newCol] = -1
                    queue.append([newRow, newCol])
            