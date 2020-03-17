# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        result = 0
        res = []
        stack = [(root, str(root.val))]
        
        while(stack):
            curr , path = stack.pop()
            
            if curr.left is None and curr.right is None:
                res.append((path))
            
            if curr.right:
                stack.append((curr.right, path + str(curr.right.val)))
            if curr.left:
                stack.append((curr.left, path + str(curr.left.val)))
            
        for s in res:
            result += int(s)
        return result
        