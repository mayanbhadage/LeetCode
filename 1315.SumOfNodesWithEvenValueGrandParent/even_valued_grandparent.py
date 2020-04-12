# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.grandparents = []
        self.sum = 0
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.traverse(root)
        
        
        for grandparent in self.grandparents:
            self.bfs(grandparent)
        
        return self.sum
        
        
    def bfs(self, root):
        
        queue = deque()
        grand_child_reached = False
        queue.append((root,0))
        while(queue):
            if not grand_child_reached:
                for _ in range(len(queue)):
                    currNode, count = queue.popleft()
                    if count == 2:
                        self.sum += currNode.val
                        grand_child_reached = True
                    
                    if currNode.left:
                        queue.append((currNode.left,count + 1))
                    if currNode.right:
                        queue.append((currNode.right,count + 1))
            else:
                break
                    
                    
        
    def traverse(self, currNode):
        if currNode is None:
            return 
        
        if currNode.val % 2 == 0:
            self.grandparents.append(currNode)
        
        self.traverse(currNode.left)
        self.traverse(currNode.right)