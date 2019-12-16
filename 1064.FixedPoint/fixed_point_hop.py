class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        
        for i in range(0,len(A),2):
            if i <= A[i]:
                if i - 1 == A[i-1]:
                    return i-1
                elif i == A[i]:
                    return i
                else:
                    return-1
                    
        
        return -1