class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Bruteforce Method
        window_start = 0
        result = []
        for window_end in range(len(nums)):
            
            window_size = window_end -  window_start + 1
            
            if window_size >= k:
                res = self.calculate_median(nums[window_start:window_end+1])
                window_start += 1
                result.append(res)
        return result
                
                
                
        
    def calculate_median(self,arr):
        arr.sort()
        len_ = len(arr)
        if len_% 2 == 0:
            num1 = arr[len_ // 2 - 1]
            num2 = arr[len_ // 2]
            return (num1 + num2)/2
        else:
            return arr[len_//2]
    

        