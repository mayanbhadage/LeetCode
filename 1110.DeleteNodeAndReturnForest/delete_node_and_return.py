# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = deque([(root,False)])
        
        delete = set(to_delete)
        result = []
        
        while queue:
            
            currNode,hasParent = queue.popleft()
            if not hasParent and currNode.val not in delete:
                result.append(currNode)
                
            hasParent = not currNode.val in delete
            
            if currNode.left:
                queue.append((currNode.left,hasParent))
                if currNode.left.val in delete:
                    currNode.left = None
            if currNode.right:
                queue.append((currNode.right,hasParent))
                if currNode.right.val in delete:
                    currNode.right = None
        return result