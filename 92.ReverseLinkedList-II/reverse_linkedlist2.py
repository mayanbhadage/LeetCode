# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        #go to m-1 pos
        curr,prev = head,None
        i = 0
        while(curr and i < m-1):
            prev = curr
            curr = curr.next
            i += 1
        
        
        #store the links 
        last_of_first = prev
        last_of_second = curr
        
        # reverse the part
        nxt = None
        i = 0
        while curr and i < n-m+1:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
            
        # join the connections
        
        if last_of_first is not None:
            last_of_first.next = prev
        else:
            head = prev
        
        last_of_second.next = curr
        
        return head
        
        