# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__ (self):
        self.arr = []
        self.count = 0
    def minDiffInBST(self, root: TreeNode) -> int:

        self.traverse(root)
        min_dist = 9999
        for i in range(1,self.count):
            temp = abs(self.arr[i] - self.arr[i-1])
            if temp < min_dist:
                min_dist = temp

        return min_dist
    
    def traverse(self,currNode):
        if currNode is None:
            return
        self.traverse(currNode.left)
        self.arr.append(currNode.val)
        self.count += 1
        self.traverse(currNode.right)