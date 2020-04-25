class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heap = []
        
        for stick in sticks:
            heapq.heappush(heap, stick)
            
        while(len(heap) > 1):
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)
            
            total = stick1 + stick2
            cost += total
            
            heapq.heappush(heap, total)
        
        return cost
            