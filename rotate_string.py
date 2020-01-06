class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        newStr = A + A
        
        return B in newStr