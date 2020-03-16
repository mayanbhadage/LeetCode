"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return
        
        queue = deque()
        queue.append(root)
        
        while(queue):
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                currNode = queue.popleft()
                curr_level.append(currNode)
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    
            for i in range(1,len(curr_level)):
                curr_level[i-1].next = curr_level[i]
            
        return root
        