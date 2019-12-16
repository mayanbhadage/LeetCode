class Solution:
    def __init__(self):
        self.found = False
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        if root1 is None or root2 is None:
            return

        self.traverse(root1,target,root2)
        #self.traverse(root2,tree2)
                
        return self.found
        
    def traverse(self,currNode,value,otherTree):
        if currNode is None:
            return
        if not self.found:
            self.binarySearch(otherTree,value-currNode.val)
            self.traverse(currNode.left,value,otherTree)
            self.traverse(currNode.right,value,otherTree)
        
    def binarySearch(self,currNode, value):
        if currNode is None:
            return
        #print (f"{currNode.val} {value}")
        if currNode.val == value:
            self.found = True
        elif currNode.val > value:
            self.binarySearch(currNode.left,value)
        else:
            self.binarySearch(currNode.right,value)
        