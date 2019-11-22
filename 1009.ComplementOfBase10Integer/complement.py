class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = "{0:b}".format(N)
        res = ""
        for c in binary:
            if c == "0":
                res += "1"
            else:
                res+= "0"
        
        return int(res,2)