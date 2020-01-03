class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            str_num = str(num)
            len_nums = len(str_num)
            if len_nums % 2 == 0:
                count += 1
        return count