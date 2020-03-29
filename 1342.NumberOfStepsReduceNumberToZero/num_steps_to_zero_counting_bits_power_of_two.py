class Solution:
    def numberOfSteps (self, num: int) -> int:
        #bit counting with power of 2
        
        steps = 0
        power = 1
        
        while(power <= num):
            
            if num & power == 0:
                steps += 1
            else:
                steps += 2
            power *= 2
        
        return steps - 1
        