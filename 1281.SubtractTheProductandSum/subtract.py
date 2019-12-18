class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p = 0,1
        
        for x in str(n):
            s += int(x)
            p *= int(x)
            
        return p - s