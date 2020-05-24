class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        #For this we need left biased binary tree and right biased binary tree
        # Left Biased binary tree
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        
        if left >= len(nums) or nums[left] != target:
            start = -1
        else:
            start = left
        
        
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
                
        if right < 0 or nums[right] != target:
            end = -1
        else:
            end = right
        
        
        
        return [start, end]