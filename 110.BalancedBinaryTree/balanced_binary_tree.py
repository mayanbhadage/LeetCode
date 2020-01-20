# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.calculate(root)[1]
    
        
        
    def calculate(self,currNode,):
        #Null Node
        if currNode is None:
            return(-1,True)
        #Left subtree
        left_result = self.calculate(currNode.left)
        if left_result[1] == False:
            return left_result
        #Right subtree
        right_result = self.calculate(currNode.right)
        if right_result[1] == False:
            return right_result
        
        isBalanced = None
        if abs(left_result[0]-right_result[0]) <= 1:
            isBalanced = True
        else:
            isBalanced = False
            
        height = max(left_result[0],right_result[0]) + 1
        
        return (height,isBalanced)
        
        