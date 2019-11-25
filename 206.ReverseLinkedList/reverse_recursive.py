class Solution:
    def __init__(self):
        self.rHead = None
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        self.reverse_rec(head);
        
        return self.rHead
        
    def reverse_rec(self,currNode):
        if(currNode.next is None):
            self.rHead = currNode
            return
        else:
            self.reverse_rec(currNode.next)
            newNode = currNode.next
            newNode.next = currNode
            currNode.next = None