class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start = 0
        matched = 0
        substr_start = 0
        min_length = len(s) + 1
        
        hmap = collections.Counter(t)
        
        #Now we try to extend the window
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in hmap:
                hmap[right_char] -= 1
                if hmap[right_char] >= 0:
                    matched += 1
            
            #Shrink the window if we can and finish as soon as we remove the matched character
            while(matched == len(t)):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                    
                left_char = s[window_start]
                window_start += 1
                
                if left_char in hmap:
                    if hmap[left_char] == 0:
                        matched -= 1
                    hmap[left_char] += 1
        if min_length > len(s):
            return ""
        
        return s[substr_start:substr_start + min_length]
            