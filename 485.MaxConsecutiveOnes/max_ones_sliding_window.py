class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_start = 0
        max_length = 0
        hmap = {}
        for window_end in range(len(nums)):
            
            if nums[window_end] == 1:
                max_length = max(max_length , window_end - window_start + 1)
            else:
                window_start = window_end + 1
        return max_length