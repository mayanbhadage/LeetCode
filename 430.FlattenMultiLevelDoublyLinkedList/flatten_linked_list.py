"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        self.flatten_rec(head, head.next)
        
        return head
        
        
    def flatten_rec(self, ptr1, ptr2):
        
        while(True):
            if ptr1.child:
                back = self.flatten_rec(ptr1.child, ptr1.child.next)
                
                ptr1.next = ptr1.child
                ptr1.child.prev = ptr1
                ptr1.child = None
                
                if back:
                    back.next = ptr2
                    ptr2.prev = back
                elif ptr2:
                    ptr1.next.next = ptr2
                    ptr2.prev = ptr1.next
                
            if ptr2 is None or ptr2.next is None:
                break
                
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
            
        return ptr2