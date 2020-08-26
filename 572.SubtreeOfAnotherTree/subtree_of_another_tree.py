# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if not s or not t:
            return False
        
        
        if self.check(s,t):
            return True
        elif self.isSubtree(s.left, t) or self.isSubtree(s.right,t):
            return True
        return False
        
    def check(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val != t.val:
            return False
        else:
            return self.check(s.left, t.left) and self.check(s.right, t.right)
        