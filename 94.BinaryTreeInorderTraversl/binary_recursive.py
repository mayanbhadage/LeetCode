# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #recursive solution
        
        if root is None:
            return
        self.traverse(root)
        return self.arr
        
    def traverse(self,currNode):
        if currNode is None:
            return
        self.traverse(currNode.left)
        self.arr.append(currNode.val)
        self.traverse(currNode.right)
        
        