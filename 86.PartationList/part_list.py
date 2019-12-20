# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.lessHead = None
        self.lessTail = None
        self.moreHead = None
        self.moreTail = None
        
    
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head is None:
            return
        
        temp = head
        
        while(temp):
            newNode = ListNode(temp.val)
            
            if temp.val < x:
                if self.lessHead is None:
                    self.lessHead = newNode
                    self.lessTail = newNode
                else:
                    self.lessTail.next = newNode
                    self.lessTail = newNode
            else:
                if self.moreHead is None:
                    self.moreHead = newNode
                    self.moreTail = newNode
                else:
                    self.moreTail.next = newNode
                    self.moreTail = newNode
            
            temp = temp.next
        if self.lessTail:       
            self.lessTail.next = self.moreHead
            return self.lessHead
        else:
            return self.moreHead