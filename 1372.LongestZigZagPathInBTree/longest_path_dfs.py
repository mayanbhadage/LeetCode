# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        stack = [(root,None, 0)]
        max_length = 0
        if not root: return 0
        while stack:
            currNode, direction, curr_length = stack.pop()
            
            
            max_length = max(curr_length, max_length)
                
            if direction == None:
                if currNode.left:
                    stack.append((currNode.left, "LEFT", curr_length+1))
                if currNode.right:
                    stack.append((currNode.right, "RIGHT", curr_length+1))
            elif direction == "LEFT":
                if currNode.right:
                    stack.append((currNode.right,"RIGHT",curr_length+1))
                if currNode.left:
                    stack.append((currNode.left, "LEFT", 1))
            else:
                if currNode.left:
                    stack.append((currNode.left,"LEFT",curr_length+1))
                if currNode.right:
                    stack.append((currNode.right, "RIGHT", 1))
        return max_length
                