# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
       #Find the middle of the linked list
        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next
            
        # now reverse the slow
        
        mid = self.reverse(slow)
        
        # itereate though both the pointers
        
        while(head and mid):
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True
        
    def reverse(self,head):
        
        prev = None
        
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
            