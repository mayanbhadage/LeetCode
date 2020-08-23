class StockSpanner:

    def __init__(self):
        self.stack = [ ]

    def next(self, price: int) -> int:
        
        current_price = price
        current_span = 1
        
        while(self.stack and self.stack[-1][0] <= current_price):
            top = self.stack.pop()
            span = top[1]
            current_span += span
        
        self.stack.append((current_price, current_span))
        
        return current_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)