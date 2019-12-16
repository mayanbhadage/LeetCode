class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        if root1 is None or root2 is None:
            return
        
        tree1 = []
        tree2 = []
        self.traverse(root1,tree1)
        self.traverse(root2,tree2)
        
        hmap = {}
        
        for num in tree1:
            hmap[target-num] = 1
        
        for num in tree2:
            if num in hmap:
                return True
        return False
        
    def traverse(self,currNode,arr):
        if currNode is None:
            return
        self.traverse(currNode.left,arr)
        arr.append(currNode.val)
        self.traverse(currNode.right,arr)