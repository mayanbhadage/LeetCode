class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)< 2:
            return 0
        index = nums.index(max(nums))
        temp = nums.copy()
        nums.sort(reverse = True)
        
        if nums[0] >= nums[1]*2:
            return index
        else:
            return -1
        