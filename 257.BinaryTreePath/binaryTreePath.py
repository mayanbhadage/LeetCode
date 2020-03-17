# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return
        
        result = []
        
        stack = [(root, str(root.val))]
        
        while(stack):
            curr, path = stack.pop()
            
            if curr.left is None and curr.right is None:
                result.append(path)
            
            if curr.right:
                stack.append((curr.right, path + "->"+ str(curr.right .val)))
            if curr.left:
                stack.append((curr.left, path + "->" + str(curr.left.val)))
            
        return result