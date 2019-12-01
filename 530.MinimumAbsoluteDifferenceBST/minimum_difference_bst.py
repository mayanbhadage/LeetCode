# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.arr = []
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traverse(root)
        min_ = 99999
        for x in range(1,len(self.arr)):
            temp = abs(self.arr[x] - self.arr[x-1])
            if temp < min_:
                min_ = temp
        return min_
        
    def traverse(self,currNode):
        if currNode is None:
            return
        self.traverse(currNode.left)
        self.arr.append(currNode.val)
        self.traverse(currNode.right)
        