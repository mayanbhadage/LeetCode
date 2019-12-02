from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = OrderedDict()
        
        uniques = list({x:0 for x in s})
        
        for x in (uniques):
            temp = s.find(x)
            hmap[x] = [s.count(x),temp ]
        
        for key,value in hmap.items():
            if value[0] == 1:
                return value[1]
        return -1
        