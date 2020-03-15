# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = self.length_of_linked_list(head)
        if length < k:
            return head
        for i in range(1,length,k):
            m = i
            n = i + k - 1
            if n <= length:
                #print(m,n)
                head = self.reverse(head,m,n)
        return head
        
    def length_of_linked_list(self,head):
        count = 0
        temp = head
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    
    def reverse(self,head,m,n):
        if m == n:
            return head
        
        # Reach to m-1th node
        
        curr,prev = head, None
        i = 0
        while(curr and i < m-1):
            prev = curr
            curr = curr.next
            i+=1
        
        #store the connections
        last_of_first_part = prev
        last_of_second_part = curr
        
        #reverse the required
        
        nxt = None
        i = 0
        while(curr and i < n-m+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i+=1
            
        #join the connections:
        if last_of_first_part:
            last_of_first_part.next = prev
        else:
            head = prev
        
        
        last_of_second_part.next = curr
        
        return head
            
        
        