class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            n = self.calculateSquare(n)
            
            if n == 1:
                return True
            elif n in visited:
                return False
            visited.add(n)
            
        
    def calculateSquare(self,num):
        str_num = str(num)
        result = 0
        for ch in str_num:
            result += int(ch) * int(ch)
        return result