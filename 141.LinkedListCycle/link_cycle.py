class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        slow_ptr = head
        fast_ptr = head.next
        
        temp = head
        
        while(temp!= None):
            if(fast_ptr == None):
                return False
            
            if(slow_ptr == fast_ptr):
                return True
            
            temp = temp.next
            slow_ptr = slow_ptr.next
            if (fast_ptr.next == None):
                return False
            fast_ptr = fast_ptr.next.next
            
            
        return False