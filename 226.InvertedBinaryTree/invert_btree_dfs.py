class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #dfs solution
        
        stack = [root]
        
        while stack:
            currNode = stack.pop()
            
            if currNode:
                currNode.left , currNode.right = currNode.right, currNode.left
                stack += [currNode.right, currNode.left]
        
        return root