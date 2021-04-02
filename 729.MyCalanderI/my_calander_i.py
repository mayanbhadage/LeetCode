class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, start, end, node):
        if node.start >= end:
            if not node.left:
                node.left = Node(start, end)
                return True
            else:
                return self.insert(start, end, node.left)
        elif node.end <= start:
            if not node.right:
                node.right = Node(start, end)
                return True
            else:
                return self.insert(start, end, node.right)
        else:
            return False


class MyCalendar:

    def __init__(self):
        self.tree = Tree()
        

    def book(self, start: int, end: int) -> bool:
        if not self.tree.root:
            self.tree.root = Node(start, end)
            return True
        return self.tree.insert(start, end, self.tree.root)