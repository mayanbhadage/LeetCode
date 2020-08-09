"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # 3 Pass Solution O(1) Space
        
        if not head: return
        #Pass1
        curr = head
        while curr:
            cloned = Node(curr.val)
            cloned.next = curr.next
            curr.next = cloned
            curr = curr.next.next
        
        #pass2
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        
        
        #Pass3 : seperate two list
        
        oldHead = p = head
        newHead = np = head.next
        
        while(p):
            p.next = np.next
            np.next = np.next.next if np.next else None
        
            p = p.next
            np = np.next
        return newHead
        