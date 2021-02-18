class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Bruteforce
        if not s: return 0
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.checkUnique(s[i:j]):
                    max_len = max(max_len, j-i)
        return max_len
    
    def checkUnique(self, string):
        hmap = defaultdict(int)
        for char in string:
            if char in hmap:
                return False
            hmap[char] += 1
        return True