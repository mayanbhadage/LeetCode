class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #The careful observation here is before unique element the first occourance is on even index and second on odd after unique its reversed
        
        #Use this observatin to apply binary search
        
        #Length is odd always so mid will be even
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) //2
            
            if mid + 1 == len(nums):
                return nums[mid]
            elif mid - 1 < 0:
                return nums[0]
            
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+ 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        
        