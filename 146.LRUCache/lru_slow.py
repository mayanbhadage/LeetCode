class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.queue = deque()
        self.hmap = {}
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            # This means the key is already present in our queue
            # So we need to make it at back of the queue
            idx = 0
            while(idx < len(self.queue)):
                if self.queue[idx] == key:
                    break
                idx += 1
            del self.queue[idx]
            self.queue.append(key)
            return self.hmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            idx = 0
            while(idx < len(self.queue)):
                if self.queue[idx] == key:
                    break
                idx += 1
            del self.queue[idx]
            self.queue.append(key)
            self.hmap[key] = value
            return
            
        if self.count >= self.capacity:
            temp = self.queue.popleft()
            del self.hmap[temp]
            self.count -= 1
            
        self.queue.append(key)
        self.hmap[key] = value
        self.count += 1
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)