class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        temp = []
        
        max_count = 0
        
        size = 0
        for i,x in enumerate(nums):
            if x == 0:
                temp.append(i)
            size +=1
        
        temp.append(size)
        
        
        
        d = 0
        for c in temp:
            z = c-d
            if z > max_count:
                max_count = z
            d = c+1
        return max_count
        
                