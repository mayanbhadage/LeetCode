class Solution:
    def removeDuplicates(self, S: str) -> str:
        #two pointer solution
        S = list(S)
        ptr1 , ptr2 = 0,0
        
        while ptr2 < len(S):
            
            S[ptr1] = S[ptr2]
            
            if ptr1 > 0 and S[ptr1] == S[ptr1-1]:
                ptr1 -= 2
            
            ptr1 += 1
            ptr2 += 1
            
        result = S[:ptr1]
        
        return "".join(result)