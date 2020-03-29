class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        open_count = 0
        
        for br in S:
            
            if br == "(" and open_count > 0:
                result.append(br)
            
            if br == ")" and open_count > 1:
                result.append(br)
            
            if br == "(":
                open_count += 1
            else:
                open_count -= 1
        return "" .join(result)