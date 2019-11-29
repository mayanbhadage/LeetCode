# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.hmap = {}
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return

        self.hmap[root.val] = k - root.val
        self.traverse(root.left,k)
        self.traverse(root.right,k)
        
        for key,value in self.hmap.items():
            if value in self.hmap and key != value:
                return True
        return False
        
        
        
    def traverse(self, currNode, k):
        if currNode is None:
            return
        else:
            self.hmap[currNode.val] = k - currNode.val
            self.traverse(currNode.left,k)
            self.traverse(currNode.right,k)
            
                