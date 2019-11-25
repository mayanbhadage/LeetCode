# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Easy way maybe not optimal
        if head is None:
            return
        
        
        mystr = ""
        temp = head
        while(temp is not None):
            mystr += str(temp.val)
            temp = temp.next
        
        num = int(mystr)
        num += 1
        print(num)
        NN = ListNode(-1)
        s_num = str(num)
        for x in s_num :
            self.appendList(NN,x)
        return NN.next
        
        
    def appendList(self, currNode, value):
        newNode = ListNode(value)
        if currNode is None:
            currNode = newNode
        else:
            while(currNode.next is not None):
                currNode = currNode.next
            currNode.next = newNode
  
        