class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        result = []
        for i in range(1,len(s)):
            if(s[i]=="+" and s[i-1]=="+"):
                res = s[:i-1] + "--" +s[i+1:]
                result.append(res)
                
        return result
        