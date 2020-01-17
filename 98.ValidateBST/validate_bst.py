class Solution:
    def __init__(self):
        self.arr = []
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        self.traverse(root)
        return self.arr == sorted(self.arr) and len(set(self.arr)) == len(self.arr)
        
        
    def traverse(self,currNode):
        if currNode is None:
            return 
        self.traverse(currNode.left)
        self.arr.append(currNode.val)
        self.traverse(currNode.right)