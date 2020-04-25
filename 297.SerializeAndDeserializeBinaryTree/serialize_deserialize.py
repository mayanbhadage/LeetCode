# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = [str(root.val)]
        queue = deque([(root,result)])
        
        while(queue):
            num_nodes = len(queue)
            for _ in range(len(queue)):
                currNode, currPath = queue.popleft()
                if currNode.left:
                    currPath.append(str(currNode.left.val))
                    queue.append((currNode.left, currPath))
                else:
                    currPath.append("null")
                if currNode.right:
                    currPath.append(str(currNode.right.val))
                    queue.append((currNode.right, currPath))
                else:
                    currPath.append("null")
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = data.split(",")
        
        r_val = int(nodes[0])
        
        root = TreeNode(r_val)
        
        queue = deque([root])
        index = 1
        while(queue):
            currNode = queue.popleft()
            
            if nodes[index] != "null":
                currNode.left = TreeNode(int(nodes[index]))
                queue.append(currNode.left)
            index += 1
            
            if nodes[index] != "null":
                currNode.right = TreeNode(int(nodes[index]))
                queue.append(currNode.right)
            index += 1
            
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))