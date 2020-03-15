# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        queue = deque()
        queue.append(root)
        result = []
        
        while(queue):
            num_nodes_at_curr_level = len(queue)
            curr_level_nodes = []
            for _ in range(num_nodes_at_curr_level):
                currNode = queue.popleft()
                curr_level_nodes.append(currNode.val)
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append( curr_level_nodes)
        return result
        