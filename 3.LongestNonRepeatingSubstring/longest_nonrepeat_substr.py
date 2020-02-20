# Hmap to store index of the chars,
# if char is already present the shift the window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        hmap = {}
        
        for window_end in range(len(s)):
            
            right_char = s[window_end]
            if right_char in hmap:
                window_start = max(window_start,hmap[right_char] + 1)
            
            hmap[right_char] = window_end
            max_length = max(max_length,window_end - window_start + 1)
        return max_length