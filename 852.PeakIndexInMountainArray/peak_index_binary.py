class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        #binary search
        
        # Find the maximum index i such that A[i] < A[i+1]        
        low = 0 
        high = len(A) - 1
        
        while(low < high):
            
            mid = (low + high)//2
            
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid
        
        return low