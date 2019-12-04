# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        temp = head
        heap = []
        while temp:
            heap.append(temp.val)
            temp = temp.next
        heap.sort()
        index = 0
        temp = head
        while temp:
            temp.val = heap[index]
            temp = temp.next
            index += 1
        return head
            
            
            