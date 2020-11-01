class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.check(s, i, i)
            even = self.check(s, i , i+1)
            
            res = max(res, even, odd, key=len)
        return res
        
        
   '''
   The while loop stops either because l or r is out of range or because the s[l] != s[r],
   which means neither s[l] nor s[r] can be part of the longest palindrome and the helper function returns s[l+1:r](inclusive on the left and exclusive on the right).
   '''     
    def check(self,s, l, r):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
        
#Time O(n^2)
#Space O(1)