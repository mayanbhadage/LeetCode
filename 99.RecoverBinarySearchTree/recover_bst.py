# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nums = []
        self.inorderTraversal(root)
        
        #Find the nodes that are not in order
        num1 , num2 = -1,-1
        for idx in range(len(self.nums) - 1):
            if self.nums[idx + 1] < self.nums[idx]:
                num2 = self.nums[idx + 1]
                
                if num1 == -1:
                    num1 = self.nums[idx]
                else:
                    break
        '''
        Inorder traversal will give sorted array, find the two values which are not in proper place
        and swap the values of that node
        
        
        '''
        self.node1 = None
        self.node2 = None
        self.traverse(root, num1, num2)
        
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
                    
    def traverse(self,node, num1, num2):
        if not node:
            return 
        self.traverse(node.left, num1, num2)
        if node.val == num1:
            self.node1 = node
        if node.val == num2:
            self.node2 = node
        self.traverse(node.right, num1, num2)
        
        
        
        
    
    def inorderTraversal(self,node):
        if not node:
            return None
        self.inorderTraversal(node.left)
        self.nums.append(node.val)
        self.inorderTraversal(node.right)
        
        