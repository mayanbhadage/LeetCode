# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.retval = None
        self.found = False
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res , stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return self.retval
            currNode = stack.pop()
            if self.found == True:
                self.retval = currNode
                stack = []
                continue
            if currNode == p:
                self.found = True
            root = currNode.right
            
        
        
        