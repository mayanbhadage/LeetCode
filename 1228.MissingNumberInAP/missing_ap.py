class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        index = -1
        max_diff = 0
        if arr[1] < arr[0]:
            arr = arr[::-1]
        for i in range(1,len(arr)):
            diff = (arr[i] -arr[i-1])
            if max_diff < diff:
                max_diff = diff
                index = i
                
        return arr[index-1] + int(max_diff/2)