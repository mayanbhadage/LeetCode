class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        left_sum = 0
        for i , num in enumerate(nums):
            sum_ -= num
            if left_sum == sum_:
                return i
            left_sum += num
        return -1
            