class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = bytearray(10**6)
        

    def add(self, key: int) -> None:
        self.arr[key] = 1
        

    def remove(self, key: int) -> None:
        self.arr[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.arr[key]