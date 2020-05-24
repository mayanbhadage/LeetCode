class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        #Binary Search Solution
        
        # Find right most index of 0 in the each rows
        # There are two cases here 
        # 1. Negative number exists in our row
        # Here the total number of negative numbers in this row will be index of 0 + 1 to end 
        
        
        # 2. Row constains all positive
        # Here index will be out of bound
        
        
         #Right Biased Binary Search
        
        count = 0
        
        for rows in grid:
            index = self.rightBiasBSearch(rows, 0)
            #print(index)
            count += (len(rows) - (index + 1) + 1)
        return count
            
            
    def rightBiasBSearch(self,nums, target):       
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = left + (right-left)//2
            
            if nums[mid] > target:
                left = mid + 1
            elif nums[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
                
        return left