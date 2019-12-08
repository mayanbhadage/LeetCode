class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.sum = 0
        self.queue = []
        self.size = size

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.queue.append(val)
            self.sum += val
            self.count += 1
        else:
            self.sum -= self.queue.pop(0)
            self.sum+= val
            self.queue.append(val)
        return(self.sum/self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)