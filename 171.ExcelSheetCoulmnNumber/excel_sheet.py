class Solution:
    def titleToNumber(self, s: str) -> int:

        sum_ = 0
        for ct,r in enumerate(reversed(s)):  
            sum_ += (ord(r) - ord('A') + 1) * (26**ct)
        return sum_