class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        
        # Check if currnt booking is causing triple overlap or not
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.bookings:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        self.bookings.append((start, end))
        return True
                                    
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)