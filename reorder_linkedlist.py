# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        
        if head is None or head.next is None:
            return head
        prev = None
        slow = head
        fast = head
        
        while(fast and fast.next):
            prev = slow
            slow = slow.next 
            fast = fast.next.next
        #Reverse from mid  
        ptr2 = self.reverse(slow)
        ptr1 = head
        prev.next = None
        
        return self.reorder(ptr1,ptr2)
        
        self.traverse(ptr1)
        self.traverse(ptr2)
    
    #Make connetions
    def reorder(self, ptr1, ptr2):
        
        while(ptr1 and ptr2):
            temp1 = ptr1
            temp2 = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
            temp1.next = temp2
            temp2.next = ptr1
        if ptr2:
            temp2.next = ptr2
            
        return ptr1
        
    def reverse(self,head):
        prev = None
        while(head):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    
    def traverse(self,head):
        temp = head
        while(temp):
            print(f"{temp.val}", end = "->")
            temp = temp.next
        print("")