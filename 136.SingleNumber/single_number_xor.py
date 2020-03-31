class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        
        return result