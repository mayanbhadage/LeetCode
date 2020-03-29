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
        if not head: return None
        
        node , stack = head, []
        
        while(node):
            
            if node.child:
                if node.next:
                    stack.append(node.next)
                
                node.next = node.child
                node.child.prev = node
                node.child = None
            
            if not node.next and stack:
                node.next = stack.pop()
                node.next.prev = node
            
            node = node.next
        
        return head