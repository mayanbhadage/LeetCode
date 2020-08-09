class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hmap = {}
        if not head: return 
        temp = head
        
        #Pass 1 just make cloned nodes and map them to original
        while(temp):
            cloned = Node(temp.val, None, None)
            hmap[temp] = cloned
            temp = temp.next
        
        currNode = head
        while(currNode):
            
            if currNode.next:
                hmap[currNode].next = hmap[currNode.next]
            if currNode.random:
                hmap[currNode].random = hmap[currNode.random]
            
            currNode = currNode.next
        return hmap[head]