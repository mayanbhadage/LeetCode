class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = collections.OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.hmap:
            self.hmap.move_to_end(key)
            return self.hmap[key]
        else:
            return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.hmap.move_to_end(key)
            self.hmap[key] = value
            return
        if len(self.hmap) >= self.capacity:
            self.hmap.popitem(last = False)
        
        self.hmap[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)