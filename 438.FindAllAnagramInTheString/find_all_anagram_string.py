class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start = 0
        
        hmap_p = collections.Counter(p)
        hmap_s = collections.defaultdict(int)
        result = []
        for window_end in range(len(s)):
            
            right_char = s[window_end]
            hmap_s[right_char] += 1
            #print(hmap_s,hmap_p)
            if window_end - window_start + 1 == len(p):
                if hmap_p == hmap_s:
                    result.append(window_start)
                left_char = s[window_start]
                
                hmap_s[left_char]  -= 1
                if hmap_s[left_char] == 0:
                    del hmap_s[left_char]
                window_start += 1
        return result
                
            