class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start_ptr = 0
        end_ptr = len(numbers) - 1
        
        while(end_ptr > start_ptr):
            curr_sum = numbers[start_ptr] + numbers[end_ptr]
            
            if curr_sum == target:
                return [start_ptr+1 , end_ptr+1]
            
            elif curr_sum > target:
                end_ptr -= 1
            
            else:
                start_ptr += 1
                
        return []