# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        stack = []
        
        stack.append((root,root.val))
        
        while(stack):
            curr, val = stack.pop()
            
            if curr.right is None and curr.left is None:
                if val == sum:
                    return True
            
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
                
        return False
            
            
            
        