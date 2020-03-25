class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        for num in nums:
            n = len(result)
            for idx in range(n):
                res = result[idx] + [num]
                if res not in result:
                    result.append(res)
        return (result)