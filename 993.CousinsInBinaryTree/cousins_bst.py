# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.hmap = {}
        self.depth = {}
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.traverse(root,None,1)
        if self.depth[x] == self.depth[y]:
            if self.hmap[x] != self.hmap[y]:
                return True
        return False
        
    def traverse(self,currNode,parentNode,depth):
        if currNode is None: 
            return
        self.traverse(currNode.left,currNode,depth+1)
        self.traverse(currNode.right,currNode,depth+1)
        if parentNode is not None:
            self.hmap[currNode.val] = parentNode.val
        self.depth[currNode.val] = depth