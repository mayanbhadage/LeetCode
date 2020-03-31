class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack = [(root,1)]
        max_height = 0
        while stack:
            
            currNode, currHeight = stack.pop()
            
            max_height = max(max_height, currHeight)
            
            if currNode.right:
                stack.append((currNode.right, currHeight + 1))
            if currNode.left:
                stack.append((currNode.left, currHeight + 1))
                
        return max_height