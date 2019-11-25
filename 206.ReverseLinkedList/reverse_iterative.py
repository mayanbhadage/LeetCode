class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Iterative Solution
        
        prevNode = None
        currNode = head
        
        while(currNode != None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        head = prevNode
        
        return head