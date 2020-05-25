class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weaker = []
        
        for i, rows in enumerate(mat):
            num_soldiers = self.left_biased_binary_search(rows, 0)
            
            weaker.append((num_soldiers, i))
            
        res = sorted(weaker, key = lambda x : (x[0],x[1]) )
        
        result = []
        if k > len(res):
            k = len(res)
        for i in range(k):
            result.append(res[i][1])
        return result
            
            
        
    def left_biased_binary_search(self,nums, target):
        #Returns number of soldier in that row
        
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            mid = low + (high - low) //2
            
            if nums[mid] == target:
                high = mid - 1
            elif nums[mid] < target:
                high = mid - 1
            elif nums[mid] > target:
                low = mid + 1
        return low