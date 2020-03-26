class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #recursive solution
        
        result = []
        self.generate_perm(nums, 0, [], result)
        return result
        
        
    def generate_perm(self,nums, idx, curr_perm, result):
        if len(curr_perm) == len(nums):
            result.append(curr_perm)
        else:
            for i in range(len(curr_perm)+1):
                new_perm = list(curr_perm)
                new_perm.insert(i,nums[idx])
                
                self.generate_perm(nums, idx+1, new_perm, result)