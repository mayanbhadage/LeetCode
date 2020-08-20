class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = Node("Head")
        self.tail = Node("Tail")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    
    def add_at_tail(self,newNode):
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        del node
        
    def isEmpty(self):
        if self.head.next == self.tail:
            return True
        
        return False
    





class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hmap = {} #Value : Node
        self.queue = DoubleLinkedList()
        self.seen = set()
        
        for num in nums:
            if num not in self.seen:
                node = Node(num)
                
                self.queue.add_at_tail(node)
                self.hmap[num] = node
                self.seen.add(num)
            else:
                if num in self.hmap:
                    self.queue.remove(self.hmap[num])
                    del self.hmap[num]
    
                
        

    def showFirstUnique(self) -> int:
        if not self.queue.isEmpty():
            return self.queue.head.next.value
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.seen:
            node = Node(value)
            
            self.queue.add_at_tail(node)
            self.hmap[value] = node
            self.seen.add(value)
        else:
            if value in self.hmap:
                self.queue.remove(self.hmap[value])
                del self.hmap[value]
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)