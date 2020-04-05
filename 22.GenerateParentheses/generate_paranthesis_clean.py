class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        self.generate( n, "", result, 0, 0)
        return result
        
        
    def generate(self, n, curr, result, open_, close_):
        if open_ < close_ or open_ > n or close_ > n:
            return
        if len(curr) == n*2:
            result.append(curr)
            return
        
        
        self.generate( n, curr + "(", result, open_+1, close_)
        self.generate( n, curr + ")" , result, open_, close_+1)