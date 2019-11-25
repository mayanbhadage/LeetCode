class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # traverse whole list if one list meets the end go to other list
        
        tempA = headA
        tempB = headB
        
        while(tempA is not tempB):
            
            if(tempA is None):
                tempA = headB
            else:
                tempA = tempA.next
            
            if(tempB is None):
                tempB = headA
            else:
                tempB = tempB.next
        
        return tempA