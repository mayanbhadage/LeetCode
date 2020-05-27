class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        #Steps to find the occourance of target number using binary search
        
        # Left Biased binary search : gives the index for First occourance
        # Right Biased binary search : gives the index for Last occourance
        
        
        left = (self.left_biased(nums,target))
        right = (self.right_biased(nums,target))
        
        if left == -1 or right == -1:
            return False
        num_occ = right - left + 1
        if num_occ > len(nums)//2:
            return True
        return False
        
    def left_biased(self,nums, target):
        
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            
            mid = low + (high - low)//2
            if nums[mid] == target:
                high = mid - 1
                
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        
        if low >= len(nums) or nums[low] != target:
            return -1 
        return low
    
    def right_biased(self,nums, target):
        
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        if high < 0 or nums[high] != target:
            return -1 
        return high
    
    
    