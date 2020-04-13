class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        ptr2 = len(S) - 1
        
        while(ptr2 >= 0):
            if S[ptr2] not in last:
                last[S[ptr2]] = ptr2
            ptr2 -= 1
        
        left = 0
        right = 0
        result = []
        
        for idx, letter in enumerate(S):
            right = max(right, last[letter])
            
            if idx == right:
                result.append(right - left + 1)
                left = right + 1
        return result