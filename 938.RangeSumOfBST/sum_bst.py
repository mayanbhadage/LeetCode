class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        range_sum = 0
        
        stack = []
        
        stack.append(root);
        
        while(len(stack) > 0):
            currentNode = stack.pop()
            
            if(currentNode != None):
                if(currentNode.val >= L and currentNode.val <= R):
                    range_sum += currentNode.val
                if(currentNode.val > L):
                    stack.append(currentNode.left)
                if(currentNode.val < R):
                    stack.append(currentNode.right)
            
            
        return range_sum