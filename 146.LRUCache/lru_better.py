class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.queue = deque()
        self.hmap = {}
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hmap[key]
        return - 1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.queue.remove(key)
            self.queue.append(key)
            self.hmap[key] = value
            return
        if self.count >= self.capacity:
            temp = self.queue.popleft()
            self.count -= 1
            del self.hmap[temp]
        self.queue.append(key)
        self.hmap[key] = value
        self.count += 1