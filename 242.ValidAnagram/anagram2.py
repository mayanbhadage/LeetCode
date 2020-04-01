class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(list(s))
        t = sorted(list(t))
        i = 0
        while (i < len(s)):
            if s[i] != t[i]:
                return False
            
            i+=1
        
        return True