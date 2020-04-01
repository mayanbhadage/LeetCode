class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # NlogN
        
        nums.sort()
        
        return nums[ (len(nums)//2)]