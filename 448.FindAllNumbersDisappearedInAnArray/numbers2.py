class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result  = []
        
        arr = [0] * len(nums)
        
        for i in range(len(nums)):
            curr = nums[i]
            arr[curr-1] = curr   
            
        for j in range(len(arr)):
            if arr[j] == 0:
                result.append(j+1)
                
        return result