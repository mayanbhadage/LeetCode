class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        
        #Find the last node of the linked list and connect it with first to form a ring
        temp = head
        n = 1 # becaus we will traverse n-1 node
        while(temp.next):
            n += 1
            temp = temp.next
        
        temp.next = head # this will form the ring
        
        #find the new head and tails
        
        new_head = head
        new_tail = None
        i = 0
        while(new_head and i != n-k % n):
            new_tail = new_head
            new_head = new_head.next
            i+=1
            
        new_tail.next = None #break the connection
        
        return new_head