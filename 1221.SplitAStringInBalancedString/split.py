class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        result = 0
        first = s[0]
        if first == "R":
            r_count += 1
        else:
            l_count += 1
        
        for ch in s[1:]:
            if ch is 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                result += 1
                r_count = 0
                l_count = 0
        return result