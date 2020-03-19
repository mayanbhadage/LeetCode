# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return  0
        max_length = 0
        d = {None:-1}
        stack = [root]
        
        while stack:
            
            curr_node= stack[-1]
            
            if curr_node.left in d and curr_node.right in d:
                curr_node = stack.pop()
                left = d[curr_node.left] + 1
                right = d[curr_node.right] + 1
                d[curr_node] = max(left,right)
                max_length = max(max_length, left + right)
            else:
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)
        return max_length
        