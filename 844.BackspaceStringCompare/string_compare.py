class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        x = self.resultString(S)
        y = self.resultString(T)
        return x == y
        
    def resultString(self,string):
        result = []
        
        for s in string:
            if s is not "#":
                result.append(s)
            else:
                if len(result) > 0:
                    result.pop()
        return result