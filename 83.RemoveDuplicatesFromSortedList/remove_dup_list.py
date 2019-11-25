class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        temp = head
        
        while(temp.next is not None):
            if(temp.val == temp.next.val):
                self.delete(temp,temp.next)
            else:
                temp = temp.next
        return head
            
            
            
    def delete(self,prevNode, currNode):
        prevNode.next = currNode.next
        currNode.next = None
        del currNode
     	
 
  	
 
 
