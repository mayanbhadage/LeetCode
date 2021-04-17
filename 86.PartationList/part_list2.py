# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        list1 = dummy = ListNode("#")
        
        curr = head
        x_pos = None
        while curr:
            if not x_pos:
                if curr.val == x:
                    x_pos = curr
            
            if curr.val < x:
                list1.next = ListNode(curr.val)
                list1 = list1.next
            curr = curr.next
            
        curr = head
        while curr != x_pos:
            if curr.val > x:
                list1.next = ListNode(curr.val)
                list1 = list1.next
            curr = curr.next
            
        curr = x_pos
        while curr:
            if curr.val >= x:
                list1.next = ListNode(curr.val)
                list1 = list1.next
            curr = curr.next
            
        return dummy.next