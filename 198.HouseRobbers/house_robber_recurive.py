class Solution:
    def rob(self, nums: List[int]) -> int:
        
        result = self.recursive(nums, len(nums) -1)
        return result
    def recursive(self,nums, idx):
        if idx < 0:
            return 0
        
        return max(nums[idx] + self.recursive(nums, idx - 2), self.recursive(nums, idx - 1))
    
    
        
        