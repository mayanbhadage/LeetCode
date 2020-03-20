class Solution:
    
    def __init__(self):
        self.min_heap = []
        self.max_heap = [] #max_heap will have negative nums
        
    def balanceHeaps(self):
        if len(self.max_heap) - len(self.min_heap) > 1:
            value = heapq.heappop(self.max_heap)
            value *= -1 
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) > len(self.max_heap):
            # we are keeping more value in max_heap in case of odd nums of elements
            value = heapq.heappop(self.min_heap)
            value *= -1
            heapq.heappush(self.max_heap, value)
            
        
        
    def insertNum(self,num): # to add the value in the heaps
        if len(self.max_heap) == 0: # Initial condition
            heapq.heappush(self.max_heap, -num)
        else:
            if num > -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        self.balanceHeaps()
        
    
    
    def removeNum(self, num): # to remove the number coming out the window
        # A new method to remove elements from heap
        try:
            idx1 = self.max_heap.index(-num)
            self.max_heap[idx1] = self.max_heap[-1]
            self.max_heap.pop()
            if idx1 < len(self.max_heap):
                heapq._siftup(self.max_heap, idx1)
                heapq._siftdown(self.max_heap, 0, idx1)
        except:
            idx1 = self.min_heap.index(num)
            self.min_heap[idx1] = self.min_heap[-1]
            self.min_heap.pop()
            if idx1 < len(self.min_heap):
                heapq._siftup(self.min_heap, idx1)
                heapq._siftdown(self.min_heap, 0, idx1)
        
        
        self.balanceHeaps()
    
    def findMedian(self, k):
        if k % 2 == 0:
            num1 = self.max_heap[0]
            num2 = self.min_heap[0]
            num1 *= -1
            return (num1 + num2)/2
        else:
            return -self.max_heap[0]
    
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window_start = 0
        result = []
        for window_end in range(len(nums)):
            self.insertNum(nums[window_end])  
            if window_end - window_start + 1 == k:
                result.append((self.findMedian(k)))
                self.removeNum(nums[window_start])
                window_start += 1
        return result