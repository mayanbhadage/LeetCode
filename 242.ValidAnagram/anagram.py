class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for x in s:
            if x in hmap:
                hmap[x] +=1
            else:
                hmap[x] = 1
        for x in t:
            if x in hmap:
                hmap[x] -= 1
            else:
                return False
            
        for value in hmap.values():
            if value != 0:
                return False
        return True