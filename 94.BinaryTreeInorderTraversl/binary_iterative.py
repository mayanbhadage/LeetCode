class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #Iterative Solution
        
        res, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            currNode = stack.pop()
            res.append(currNode.val)
            root = currNode.right
        