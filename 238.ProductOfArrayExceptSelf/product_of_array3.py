class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Two pass solution maybe
        
        result = []
        temp = 1
        
        #Forward pass
        i = 0
        while i < len(nums):
            result.append(temp)
            temp *= nums[i]
            i += 1
        
        #backward pass
        j = len(nums) - 1
        temp = 1
        
        while(j >= 0):
            result[j] *= temp
            temp *= nums[j]
            j -= 1
        return result