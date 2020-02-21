class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_start = 0
        max_ones_count = 0
        max_length = 0
        
        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                max_ones_count += 1
            if window_end - window_start + 1 - max_ones_count > 1:
                left_num = nums[window_start]
                if left_num == 1:
                    max_ones_count -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length