class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        result = []
        for i in range(1 , len(nums)+1):
            result.append(i)
        
        return(list(set(result)-set(nums)))