class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root, None, None)
        return self.sum
        
    def dfs(self, currNode, parent, grandparent):
        if currNode is None:
            return
        
        if parent and grandparent and grandparent.val % 2 == 0:
            self.sum += currNode.val
            
        self.dfs(currNode.left, currNode, parent)
        self.dfs(currNode.right, currNode, parent)