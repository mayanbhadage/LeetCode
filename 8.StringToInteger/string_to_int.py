class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        
        max_int = (2 ** 31) - 1
        min_int = (-2 ** 31)
        
        i = 0
        #1. Skip white space
        while i < len(s) and s[i] == " ":
            i += 1
            
        if i < len(s):
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                sign = 1
                i += 1
        digits = set("1234567890")
        
        while i < len(s):
            if s[i] in digits:
                result = result * 10 + int(s[i])
                i += 1
            else:
                break
        result = sign * result
        
        if result < 0:
            return max(min_int, result)
        else:
            return min(max_int, result)
    
    
    
    
        