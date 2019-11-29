class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       #convert into int add find difference
        sum_t = 0
        for x in t:
            sum_t += ord(x)
        
        for y in s:
            sum_t-= ord(y)
        return chr(sum_t)
            