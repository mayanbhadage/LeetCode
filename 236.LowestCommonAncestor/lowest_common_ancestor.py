# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if p == q:
            return p
        
        hmap_node_parent = {root: None}
        
        queue = deque([root])
        
        while(queue):
            currNode = queue.popleft()
            
            if currNode.left:
                hmap_node_parent[currNode.left] = currNode
                queue.append(currNode.left)
            if currNode.right:
                hmap_node_parent[currNode.right] = currNode
                queue.append(currNode.right)
        
        
        
        p_stack = []
        q_stack = []
        
        
        while p:
            p_stack.append(p)
            p = hmap_node_parent[p]
            
        while q:
            q_stack.append(q)
            q = hmap_node_parent[q]
            
            
        t = None
        while( p_stack and q_stack and p_stack[-1] == q_stack[-1]):
            t =  p_stack.pop()
            q_stack.pop()
            
        return t
        