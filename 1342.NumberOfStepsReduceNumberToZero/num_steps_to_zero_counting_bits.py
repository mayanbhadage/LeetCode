class Solution:
    def numberOfSteps (self, num: int) -> int:
        #Bit counting
        
        # count 2 steps if bit is 1 except for the last 1(MSB)
        #count 1 step if bit is 0
        
        if num == 0:
            return 0
        
        steps = 0
        
        binary = bin(num)[2:]
        
        for b in binary:
            if b == "1":
                steps +=2
            else:
                steps += 1
            
        return steps - 1