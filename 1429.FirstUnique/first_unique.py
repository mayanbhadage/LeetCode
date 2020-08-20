class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hmap = Counter(nums)
        
        

    def showFirstUnique(self) -> int:
        
        for key, values in self.hmap.items():
            if values == 1:
                return key
        
        return -1
        

    def add(self, value: int) -> None:
        self.hmap[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)