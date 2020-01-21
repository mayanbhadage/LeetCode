# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque()
        self.flag = False
        
    def helper(self):
        stack = []
        while True:
            while self.root:
                stack.append(self.root)
                self.root = self.root.left
            if not stack:
                self.flag = True
                return
            currNode = stack.pop()
            self.queue.append(currNode)
            self.root = currNode.right
        
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.flag:
            self.helper()
        retval = self.queue.popleft()
        return retval.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.flag:
            self.helper()
        return len(self.queue)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()