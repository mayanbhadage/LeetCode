# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return self.res
        while(True):
            result = []
            self.dfs(root, None, result)
            self.res.append(result)
            if len(result) == 1 and result[0] == root.val:
                break
        return self.res
        
    def dfs(self, currNode, parent, result):
        if currNode is None:
            return
        if currNode.left is None and currNode.right is None:
            result.append(currNode.val)
            if parent:
                if parent.left == currNode:
                    parent.left = None
                elif parent.right == currNode:
                    parent.right = None
        else:
                
            self.dfs(currNode.left, currNode, result)
            self.dfs(currNode.right, currNode, result)