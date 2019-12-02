from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        List = []
        for x in set(s):
            if s.count(x) == 1:
                List.append(s.find(x))
        
        if len(List):
            return min(List)
        else:
            return -1