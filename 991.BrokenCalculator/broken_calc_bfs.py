#BFS solution works but not on leetcode

from collections import deque
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0
        if X > Y:
            return X-Y
        return self.bfs(X,Y)
    
    def bfs (self,start, end):
        queue = deque()
        count = 0
        visited = set()
        queue.append((start,count))
        visited.add(start)
        
        while(queue):
            curr_val,count = queue.popleft()
            #perform two operations on currVal
            if curr_val == end:
                     return count
            val1 = curr_val - 1
            val2 = curr_val *2
            
                
            
            if val1 not in visited:
                queue.append((val1,count+1))
                visited.add(val1)
            if val2 not in visited and val2 < end:
                queue.append((val2,count+1))
                visited.add(val2)
            
                
                
                
                
        
