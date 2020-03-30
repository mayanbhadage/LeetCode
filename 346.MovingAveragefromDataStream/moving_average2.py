class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        
        self.size = size
        self.arr = deque()
        self.count = 0
        
        

    def next(self, val: int) -> float:
        
        self.count += 1
        self.arr.append(val)
        
        if self.count > self.size:
            self.arr.popleft()
            self.count -= 1
            
        return sum(self.arr) / len(self.arr)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)