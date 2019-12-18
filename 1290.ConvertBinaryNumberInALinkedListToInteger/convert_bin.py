class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ""
        
        temp = head
        while(temp != None):
            binary+= str(temp.val)
            temp = temp.next
        
        return int(binary,2)