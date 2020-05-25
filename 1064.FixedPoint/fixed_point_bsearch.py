class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        # Binary Search
        
        low = 0
        high = len(A) - 1
        
        while(low <= high):
            mid = low + (high-low)//2
            
            if A[mid] == mid:
                high = mid - 1
            elif A[mid] < mid:
                low = mid + 1
            else:
                high = mid - 1
                
                
        if low < len(A) and A[low] == low:
            return low
        return -1