class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root