# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return
        else:
            head = ListNode(-1)
            self.merge(l1,l2,head)
            
            return head.next
        
    def merge(self, l1 , l2 , node):
        if l1 is None and l2 is None:
            return
        elif l1 is not None and l2 is None:
            node.next = l1
            return
        elif(l1 is None and l2 is not None):
            node.next = l2
            return
        else:
            if l1.val <= l2.val:
                newNode = ListNode(l1.val)
                node.next = newNode
                self.merge(l1.next,l2,newNode)
            else:
                newNode = ListNode(l2.val)
                node.next = newNode
                self.merge(l1,l2.next,newNode)