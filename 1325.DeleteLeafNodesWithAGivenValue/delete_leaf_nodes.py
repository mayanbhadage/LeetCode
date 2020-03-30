# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        if root.left:
            #either the same node or none(if it is a leaf node and its value is equal to target) 
            root.left = self.removeLeafNodes(root.left, target)
        
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
            
        
        if root.left is None and root.right is None and root.val == target:
            return None
        else:
            return root