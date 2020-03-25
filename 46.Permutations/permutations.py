class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_length = len(nums)
        perm = deque()
        perm.append([])
        
        for curr_num in nums:
            n = len(perm)
            
            for _ in range(n):
                old_perm = perm.popleft()
                
                for j in range(len(old_perm) + 1):
                    new_perm = list(old_perm)
                    new_perm.insert(j,curr_num)
                    
                    if len(new_perm) == nums_length:
                        result.append(new_perm)
                    else:
                        perm.append(new_perm)
                        
        return result