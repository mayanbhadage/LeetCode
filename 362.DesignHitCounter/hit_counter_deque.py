class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #Deque Solution
        
        self.queue= deque()
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and (timestamp - self.queue[0]) >= 300:
            self.queue.popleft()
        return len(self.queue)