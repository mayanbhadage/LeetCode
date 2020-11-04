class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        product = 1
        zeros_count = 0
        
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                product *= num
        
        if zeros_count > 1:
            return result
        elif zeros_count == 1:
            return [0 if num != 0 else product for num in nums]
        else:
            return [int(product/num) for num in nums]