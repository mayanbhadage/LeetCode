# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = list1 = ListNode("#")
        dummy2 = list2 = ListNode("#")
        
        curr = head
        while curr:
            if curr.val < x:
                list1.next = curr
                list1 = list1.next
            else:
                list2.next = curr
                list2 = list2.next
            curr = curr.next
        list2.next = None   
        list1.next = dummy2.next
        return dummy1.next