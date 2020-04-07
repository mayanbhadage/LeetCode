class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        while(low < high):
            
            mid = (low + high)//2
            
            curr_cap = 0
            count = 1
            
            for num in nums:
                curr_cap += num
                
                if curr_cap > mid:
                    curr_cap = num
                    count += 1
            
            if count > m:
                low = mid + 1
            
            else:
                high = mid
        
        return low