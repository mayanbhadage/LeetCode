class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        origin = [0,0]
        
        heap = []
        for point in points:
            distance = self.calculate_distance(origin, point)
            heapq.heappush(heap, (distance, point))
        
        result = []
        while(K):
            dist, point = heapq.heappop(heap)
            result.append(point)
            K-= 1
        return result
    
    def calculate_distance(self, point1, point2):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        return distance