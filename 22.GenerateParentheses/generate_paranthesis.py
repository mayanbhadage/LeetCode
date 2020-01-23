class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.generate(n,output,"",0,0)
        return output
    
    def generate(self, n, output,string,open_ct,close_ct):
        if len(string) == n*2:
            if string[-1] == ')' and open_ct == close_ct:
                output.append(string)
            return
        self.generate(n,output,string+"(",open_ct+1,close_ct)
        if string:
            if open_ct > close_ct:
                self.generate(n,output,string+")",open_ct,close_ct+1)