class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            even = self.check(s, i, i)
            odd = self.check(s, i , i+1)
            
            res = max(res, even, odd, key=len)
        return res
        
        
        
    def check(self,s, l, r):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
        
#Time O(n^2)
#Space O(1)