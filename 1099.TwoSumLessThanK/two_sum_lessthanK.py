class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        
        ptr1 = 0
        ptr2 = len(A) - 1
        max_ = -math.inf
        while(ptr1 < ptr2):
            currSum = A[ptr1] + A[ptr2]
            
            if currSum < K:
                max_ = max(max_, currSum)
                ptr1 += 1
            else:
                ptr2 -= 1
        
        if max_ == -math.inf:
            return -1
        else:
            return max_