# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        carry = 0
        
        while l1 or l2 or carry:
            if l1 and l2:
                add = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                add = l1.val + carry
                l1 = l1.next
            elif l2:
                add = l2.val + carry
                l2 = l2.next
            elif carry:
                add = carry
                
            
            if add >= 10:
                    
                    carry = add//10
                    add = add % 10
            else:
                    carry = 0
            node = ListNode(add)
            curr.next = node
            curr = curr.next
            
        return dummy.next
                