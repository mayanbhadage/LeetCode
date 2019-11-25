class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if head is None:
            return
        if head.val == val:
            self.remove(head,head.next,val)
            head = head.next
        else:    
            self.remove(head,head.next,val)
        
        return head
    def remove(self,prevNode, currNode, val):
        
        if(currNode is None):
            return
         
        if(currNode.val == val):
            prevNode.next = currNode.next
            currNode.next = None
            del currNode
            self.remove(prevNode,prevNode.next,val)
        else:
            self.remove(prevNode.next,currNode.next,val)