# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        
        max_depth = 0
        while(queue):
            max_depth += 1
            
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    
        return max_depth