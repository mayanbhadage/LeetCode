class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        ptr1 = 0
        ptr2 = len(nums)- 1
        
        while(ptr1 < len(nums) - 1 and nums[ptr1] <= nums[ptr1+ 1]):
            ptr1 += 1
            
        while(ptr2 > 0 and nums[ptr2] >= nums[ptr2 - 1] ):
            ptr2 -= 1
            
        temp = nums[ptr1:ptr2+1]
        if len(temp) == 0:
            return 0
        min_ = min(temp)
        max_ = max(temp)
        
        while(ptr1 > 0 and nums[ptr1-1] > min_):
            ptr1 -= 1
            
        while(ptr2 < len(nums) - 1 and nums[ptr2 + 1] < max_):
            ptr2 += 1
            
        return ptr2 - ptr1 + 1
            
                
                
            
            
            
            
            
            
                