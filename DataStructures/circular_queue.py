class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        
        """
        
        self.circularQueue = [None] * k
        self.size = k
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            self.circularQueue[self.tail] = value
        else:
            if self.tail + 1 == self.size:
                self.tail = 0
                self.circularQueue[self.tail] = value
            else:
                self.tail = self.tail+1
                self.circularQueue[self.tail] = value
        return True
        
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.circularQueue[self.head] = None
            self.head = -1
            self.tail = -1
        
        else:
            if self.head + 1 == self.size:
                self.circularQueue[self.head] = None 
                self.head = 0
            else:
                self.circularQueue[self.head] = None 
                self.head += 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.circularQueue[self.head]
        else:
            return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.circularQueue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        
        if self.tail + 1 == self.size:
            if self.head == 0:
                return True
            else:
                return False
        else:
            if self.tail + 1 == self.head:
                return True
            else:
                return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()