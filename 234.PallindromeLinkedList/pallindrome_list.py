class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        if head is None:
            return True
        
        slow_ptr = head
        fast_ptr = head
        
        while(fast_ptr != None):
            nums.append(slow_ptr.val)
            
            if(fast_ptr.next is None):
                break
            if (fast_ptr.next.next is None):
                #nums.append(slow_ptr.next.val)
                slow_ptr = slow_ptr.next
                break
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        while(slow_ptr is not None):
            x = nums.pop()
            print(slow_ptr.val)
            if x != slow_ptr.val:
                return False
            else:
                
                slow_ptr = slow_ptr.next
        return True
        