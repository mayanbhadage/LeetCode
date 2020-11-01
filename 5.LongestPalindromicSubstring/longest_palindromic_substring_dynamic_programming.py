class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        
        dp = [[0] * len(s) for _ in range(len(s))]
        result = ""
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                result = s[i:i+2]
                
        if not result:
            result = s[0]
        
        max_len = 0
        
        for d  in range(2, len(s)):
            for i in range(len(s) - d):
                j = i + d
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    if d > max_len:
                        maxD = d;
                        result = s[i:j + 1];
                
        return result
