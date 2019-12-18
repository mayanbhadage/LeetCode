from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.hmap = OrderedDict()
        self.max_height = 0
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is not None:
            self.traverse(root,0)
            result = [None] * (self.max_height +1)
            
            for key , values in self.hmap.items():
                length = len(values)
                sum_ = sum(values)
                result[key] = sum_/length
            return result
            
            
    def traverse(self,currNode,height):
        if currNode is None:
            return
        if self.max_height < height:
            self.max_height = height
        
        if height in self.hmap:
            self.hmap[height].append(currNode.val)
        else:
            self.hmap[height] = [currNode.val]
            
        self.traverse(currNode.left,height+1)
        self.traverse(currNode.right,height+1)