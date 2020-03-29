# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        #Divide and conquer
        
        size = 0
        temp = head
        while(temp):
            size += 1
            temp = temp.getNext()
        
        self.divide_and_conquer(head, size)
            
        
    def divide_and_conquer(self, head, size):
        
        if size > 1:
            
            second_half = head
            
            for _ in range(size//2):
                second_half = second_half.getNext()
                
            self.divide_and_conquer(second_half, size - size//2) #first second half
            self.divide_and_conquer(head, size//2)
            
            
        elif(size != 0):