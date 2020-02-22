class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window_start = 0
        
        hmap_s1 = collections.Counter(s1)
        hmap_s2 = collections.defaultdict(int)
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            hmap_s2[right_char] += 1
            if window_end - window_start + 1 == len(s1):
                #print(hmap_s1, hmap_s2)
                if hmap_s2 == hmap_s1:
                    return True
                hmap_s2[s2[window_start]] -= 1
                if hmap_s2[s2[window_start]] < 1:
                    del hmap_s2[s2[window_start]]
                window_start += 1
        return False