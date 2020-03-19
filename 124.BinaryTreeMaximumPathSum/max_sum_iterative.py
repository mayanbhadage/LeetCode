
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        d = {None:0}
        stack = [root]
        max_sum = -math.inf
        
        while(stack):
            curr_node = stack[-1]
            
            if curr_node.left in d and curr_node.right in d:
                node = stack.pop()
                left = max(0, d[node.left])
                right = max(0, d[node.right])
                
                d[node]  = max(left, right) + node.val
                max_sum = max(max_sum, left + right + node.val)
            else:
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)
                    
        return max_sum