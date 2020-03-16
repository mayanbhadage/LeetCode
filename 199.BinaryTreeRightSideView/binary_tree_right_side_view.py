# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        
        result = []
        queue = deque()
        
        queue.append(root)
        
        while(queue):
            num_nodes = len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                currNode = queue.popleft()
                curr_level.append(currNode.val)
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(curr_level[-1])
        return result