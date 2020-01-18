# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        result = []
        queue = collections.deque()
        queue.append(root)
        while(queue):
            
            temp = []
            length = len(queue)
            for i in range(length):
                currNode = queue.popleft()
                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                    queue.append(currNode.right)
                    
                temp.append(currNode.val)
                
            result.append(temp)
            
                
            
        return result
            