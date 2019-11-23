class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        while(i < size):
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop() 
                i+=2
            else:
                i+=1