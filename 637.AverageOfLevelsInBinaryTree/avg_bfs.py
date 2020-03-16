# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            num_nodes= len(queue)
            curr_level = []
            
            for _ in range(num_nodes):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                    
            result.append(sum(curr_level)/len(curr_level))
        return result
        