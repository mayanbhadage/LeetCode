# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.tree1 = []
        self.tree2 = []
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        self.traverse(p,1)
        self.traverse(q,2)
        print(self.tree1)
        return self.tree1 == self.tree2
        
    def traverse(self,currNode,tree):
        if currNode is None:
            return
        
        if currNode.left is None and currNode.right is not None:
            if tree == 1:
                self.tree1.append("None")
            else:
                self.tree2.append("None")
            
            
        self.traverse(currNode.left,tree)
        
        
        
        if tree == 1:
            self.tree1.append(currNode.val)
        else:
            self.tree2.append(currNode.val)
            
        if currNode.left is not None and currNode.right is None:
            if tree == 1:
                self.tree1.append("None")
            else:
                self.tree2.append("None")
            
        self.traverse(currNode.right,tree)