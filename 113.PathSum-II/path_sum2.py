# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        if root is None:
            return
        
        result = []
        stack = [(root,[root.val])]
        while stack:
            curr, ls = stack.pop()
            
            if curr.right is None and curr.left is None:
                if sum(ls) == sums:
                    result.append(ls)
            if curr.right:
                stack.append((curr.right, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls + [curr.left.val]))
        return result
        