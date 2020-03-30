class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.count = 0
        self.array = deque()
        self.sum = 0
    def next(self, val: int) -> float:
        
        self.count += 1
        self.array.append(val)
        self.sum += val
        
        if self.count > self.size:
            value = self.array.popleft()
            self.sum -= value
            self.count -= 1
        
        return self.sum/ self.count