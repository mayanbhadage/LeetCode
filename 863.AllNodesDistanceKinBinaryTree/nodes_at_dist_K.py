# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root is None:
            return []
        #Construct two hmap
        hmap_node_parent = {root:None}
        hmap_parent_child = defaultdict(list)
        
        queue = deque([root])
        
        while(queue):
            currNode = queue.popleft()
            
            if currNode.left:
                hmap_node_parent[currNode.left] = currNode
                hmap_parent_child[currNode].append(currNode.left)
                queue.append(currNode.left)
            else:
                hmap_parent_child[currNode].append(currNode.left)
                
            if currNode.right:
                hmap_node_parent[currNode.right] = currNode
                hmap_parent_child[currNode].append(currNode.right)
                queue.append(currNode.right)
            else:
                hmap_parent_child[currNode].append(currNode.right)
        
        
        result = []
        queue = deque([(target, 0)])
        visited = set()
        while(queue):
            currNode, count = queue.popleft()
            if count == K:
                result.append(currNode.val)
                continue
            
            visited.add(currNode)
            
            if hmap_parent_child[currNode] and count < K:
                if hmap_parent_child[currNode][0] and hmap_parent_child[currNode][0] not in visited:
                    queue.append((hmap_parent_child[currNode][0],count + 1))
                if hmap_parent_child[currNode][1] and hmap_parent_child[currNode][1] not in visited:
                    queue.append((hmap_parent_child[currNode][1],count + 1))
            if hmap_node_parent[currNode] and count < K and hmap_node_parent[currNode] not in visited :
                queue.append((hmap_node_parent[currNode],count+1))
        return result
            
        
        
        
        
        