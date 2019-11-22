class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        list_nums = []
        size = 0
        for  list_ in nums:
            for val in list_:
                list_nums.append(val)
                size+=1
        
        print(list_nums)
        if (r*c) != size:
            return nums
        
        result = []
        for i in range(0,len(list_nums),c):
            result.append(list_nums[i:i+c])
            
        return result