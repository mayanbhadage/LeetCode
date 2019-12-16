class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        start = 0
        end = len(A) -1
        
        while(start < end):
            mid = (start + end)//2
            if mid < A[mid]:
                end = mid - 1
            elif mid > A[mid]:
                start = mid+1
            else:
                end = mid
        
        return start if A[start] == start else -1