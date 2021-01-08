class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        steps = 0
        queue = deque([(0,0,0)])
        directions = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]
        visited  = set([(0,0)])
        while queue:
            currX, currY  , currsteps = queue.popleft()
            
            if currX == x and currY == y:
                return currsteps
            for d in directions:
                if (currX + d[0], currY+ d[1]) not in visited:
                    visited.add((currX + d[0], currY + d[1]))
                    queue.append((currX + d[0],currY + d[1], currsteps + 1))
