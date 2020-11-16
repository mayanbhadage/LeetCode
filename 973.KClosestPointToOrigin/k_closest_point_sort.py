class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        #Input Validation
        if len(points) == 0 or K == 0:
            return []
        if K >= len(points):
            return points
        
        
        result = []
        
        for point in points:
            
            x, y = point
            dist = (x * x)  + (y * y)
            
            result.append((x,y,dist))
        
        result.sort(key = lambda x:x[2])
        
        return [[x,y] for x, y,_ in result][:K]
            
        
        
        
        