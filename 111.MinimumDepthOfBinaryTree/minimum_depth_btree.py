# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        min_depth = 0
        
        while(queue):
            min_depth += 1
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                currNode = queue.popleft()
                curr_level.append(currNode)
                if currNode.left is None and currNode.right is None:
                    return min_depth
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    
        return -1
                    
        