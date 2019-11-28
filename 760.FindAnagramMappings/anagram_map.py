class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        mapB = {v:k for k,v in enumerate(B)}
        
        result = []
        for num in A:
            result.append(mapB[num]) 
        return result;