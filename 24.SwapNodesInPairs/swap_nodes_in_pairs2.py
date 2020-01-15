# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        node1 = head
        node2 = head.next
        
        temp = node2.next
        
        node2.next = node1
        head = node2
        node1.next = self.swapPairs(temp)
        
        return head
        
    
        