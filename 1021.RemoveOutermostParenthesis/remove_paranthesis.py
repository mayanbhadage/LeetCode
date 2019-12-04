class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        open_count= 0
        result = ""
        for x in S:
            if x is "(":
                if open_count is not 0:
                    result += x
                open_count += 1
            else:
                if x is ")":
                    if open_count is not 1:
                        result += ")"
                open_count -= 1
        return(result)