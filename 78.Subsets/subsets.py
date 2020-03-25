class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #BFS approach
        
        result = [[]]
        
        for num in nums:
            temp = len(result)
            
            res = []
            for value in range(temp):
                res = result[value] + [num]
                result.append(res)
        return result
        