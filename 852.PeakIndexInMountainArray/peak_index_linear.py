class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A)):
            if A[i-1] - A[i] > 0:
                return i-1
            