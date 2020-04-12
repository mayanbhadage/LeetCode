class Solution:
    def __init__(self):
        self.sorted_nodes = []
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        
        temp = 0
        idx = len(self.sorted_nodes) -1 
        while(idx >= 0):
            self.sorted_nodes[idx].val += temp 
            temp = self.sorted_nodes[idx].val
            idx -= 1
        
        return root
        
        
    def traverse(self, currNode):
        if currNode is None:
            return
        
        self.traverse(currNode.left)
        self.sorted_nodes.append(currNode)
        self.traverse(currNode.right)