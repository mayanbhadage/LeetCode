# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return
        
        queue = deque()
        parent = collections.defaultdict(list)
        queue.append((root,0))
        
        while(queue):
            curr_level = []
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                currNode, currHeight = queue.popleft()
                curr_level.append(currNode)
                if currNode.left:
                    queue.append((currNode.left,currHeight+1))
                    parent[currNode.left] = currNode
                if currNode.right:
                    queue.append((currNode.right,currHeight+1))
                    parent[currNode.right] = currNode
                    
        
        
        
        while(len(curr_level) > 1):
            s = set()
            for node in curr_level:
                s.add(parent[node])
            curr_level = list(s)
        
        return curr_level[0]
    
        