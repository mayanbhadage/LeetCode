class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left , right , count , product = 0, 0, 0, 1
        while(right < len(nums)):
            product *= nums[right]
            right += 1
            
            while(right > left and product >= k):
                product /= nums[left]
                left += 1
            count += right - left
            
        return count