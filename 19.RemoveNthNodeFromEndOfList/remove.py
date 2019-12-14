class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        runner = head
        
        while n > 0:
            runner = runner.next
            n -= 1
        if runner is None:
            return head.next
        while runner.next != None:
            current = current.next
            runner = runner.next
        
        current.next = current.next.next
        
        return head