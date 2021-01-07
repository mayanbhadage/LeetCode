class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        self.memo = {}
        
        return self.helper(s)
        
    def helper(self, s):
        if len(s) == 0:
            return 1
        if s in self.memo:
            return self.memo[s]
        
        one = two = 0
        
        if int(s[:1]) > 0 and int(s[:1]) < 10:
            one = self.helper(s[1:])
        if int(s[:2]) > 9 and int(s[:2]) < 27:
            two = self.helper(s[2:])
        self.memo[s] = one + two
        
        return self.memo[s]