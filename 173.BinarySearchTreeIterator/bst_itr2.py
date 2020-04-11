# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = deque()
        self.traverse(root)
        
    def traverse(self,currNode):
        if currNode is None:
            return
        self.traverse(currNode.left)
        self.stack.append(currNode.val)
        self.traverse(currNode.right)
    

    def next(self) -> int:
        """
        @return the next smallest number
        """
        currNode = self.stack.popleft()
        return currNode
        
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.stack:
            return False
        else:
            return True
        