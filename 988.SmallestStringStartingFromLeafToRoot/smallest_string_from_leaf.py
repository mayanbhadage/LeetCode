# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root is None:
            return
        
        paths = []
        
        stack = [(root, chr(root.val + ord('a')))]
        
        while(stack):
            curr, char = stack.pop()
            
            if curr.right is None and curr.left is None:
                char = char[::-1]
                paths.append(char)
            
            if curr.right:
                stack.append((curr.right, char + chr(curr.right.val + ord('a'))))
            if curr.left:
                stack.append((curr.left, char + chr(curr.left.val + ord('a'))))
            
        paths.sort()
        return paths[0]
        