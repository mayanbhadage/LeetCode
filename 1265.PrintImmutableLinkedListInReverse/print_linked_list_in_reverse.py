class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        
        temp = head
        
        while(temp):
            stack.append(temp)
            temp = temp.getNext()
            
        while(stack):
            val = stack.pop()
            val.printValue()
        