class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.calculateSquare(n)
        if fast == 1:
            return True
        
        while(slow != fast):
            
            slow = self.calculateSquare(slow)
            fast = self.calculateSquare(fast)
            fast = self.calculateSquare(fast)
            if fast == 1:
                return True
        return False
        
    def calculateSquare(self,num):
        str_num = str(num)
        result = 0
        for ch in str_num:
            result += int(ch) * int(ch)
        return result