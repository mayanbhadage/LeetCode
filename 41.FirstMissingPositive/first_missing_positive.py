class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(-1) # For corner case: 
        i = 0
        n = len(nums)
        
        if n < 1:
            return n + 1
        
        while(i < n):
            
            if nums[i] != i + 1: # this means the number is in incorrect position
                if nums[i]  < 0: # we skip if the number is less than 0
                    i += 1
                elif nums[i] >= len(nums): # we cannot swap because of index will go out of range
                    i += 1
                elif nums[i] == nums[nums[i] -1]: # numbers are not duplicate
                    i += 1
                else:
                    nums[nums[i] -1],nums[i] = nums[i], nums[nums[i] -1]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return 1