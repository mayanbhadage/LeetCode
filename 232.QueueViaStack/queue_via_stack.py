class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.temp_buffer = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.temp_buffer) != 0:
            while len(self.temp_buffer):
                value = self.temp_buffer.pop()
                self.stack.append(value)
        
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        while(len(self.stack)):
            val = self.stack.pop()
            self.temp_buffer.append(val)
        ret_val = self.temp_buffer.pop()
        return ret_val
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        if len(self.temp_buffer) != 0:
            return self.temp_buffer[-1]
        
        while(len(self.stack)):
            val = self.stack.pop()
            self.temp_buffer.append(val)
        return self.temp_buffer[-1]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) == 0 and len(self.temp_buffer) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()