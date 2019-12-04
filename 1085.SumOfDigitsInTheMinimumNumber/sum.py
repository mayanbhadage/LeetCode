class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        A.sort()
        x = A[0]
        
        suM = 0;
        
        while(x / 10 > 0 or x % 10 > 0):
            suM += int(x % 10)
            x = x/10
        if(suM % 2 == 0):
            return 1
        else:
            return 0
            