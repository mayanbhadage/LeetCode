class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        idx = -math.inf
        
        result = [0] * len(S)
        
        for i in range(len(S)):
            if S[i] == C:
                idx = i
            result[i] = i - idx
            
        idx = math.inf
        for i in reversed(range(len(S))):
            if S[i] == C:
                idx = i
            result[i] = min(result[i], idx-i)
        
        return result