class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        Assend = A.copy()
        Assend.sort()
        Decend = Assend[::-1]
        
        return A == Assend or A == Decend