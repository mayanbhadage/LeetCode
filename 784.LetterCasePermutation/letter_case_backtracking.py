class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(substring,index):
            if len(substring) == len(S):
                result.append(substring)
            else:
                if S[index].isalpha():
                    backtrack(substring+S[index].swapcase(),index+1)
                backtrack(substring+S[index],index+1)
                
        substr = ""
        result = []
        index = 0
        backtrack(substr,index)
        return result