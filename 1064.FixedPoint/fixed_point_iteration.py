class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(0,len(A)):
            if i == A[i]:
                return i
            
                    
        return -1