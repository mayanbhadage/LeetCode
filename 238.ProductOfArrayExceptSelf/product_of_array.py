class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # To solve this we need two pass
        
        #First Forward Pass where we calculate the product for forward pass
        left_product = [1] * len(nums)
        
        for i in range(1,len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        #Second Pass: Backward pass to calculate the product after certain element
        right_product = [1] * len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            right_product [i] =  right_product [i+1] * nums[i+1]
            
        return [left_product[i] * right_product[i] for i in range(len(nums)) ]