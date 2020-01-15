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
        
        temp_node = ListNode(node2.val)
        
        temp_node.next = node1
        head = temp_node
        
        node1.next = self.swapPairs(node2.next)
        del node2
        return head
        

    
        