class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        max_repeat = 0
        max_length = 0
        hmap = collections.defaultdict(int)
        for window_end in range(len(s)):
            right_char = s[window_end]
            hmap[right_char] += 1
            max_repeat = max(max_repeat,hmap[right_char])
            #if window_size - max_repeat > k -> shrink the sliding window from start
            if window_end - window_start + 1 - max_repeat > k:
                left_char = s[window_start]
                hmap[left_char] -= 1
                window_start += 1
                
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length