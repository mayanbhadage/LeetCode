class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.count:
            heapq.heappush(self.max_heap, -num)
            self.count += 1
            return
        if num  <= self.max_heap[0] * -1:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.count += 1
        
        if  len(self.max_heap) - len(self.min_heap) > 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-val)
            
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
        

    def findMedian(self) -> float:
        
        if self.count % 2 == 0:
            
            val1 = self.max_heap[0]
            val2 = self.min_heap[0]

            val1 = val1 * -1

            return (val1 + val2) /2
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()