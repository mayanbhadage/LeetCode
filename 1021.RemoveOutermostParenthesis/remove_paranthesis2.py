class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        
        open_cnt = 0
        close_cnt = 0
        res = deque()
        for br in S:
            
            if br == '(':
                open_cnt += 1
            else:
                close_cnt += 1
            if  open_cnt == close_cnt:
                open_cnt = 0
                close_cnt = 0
                res.popleft()
                result.append(res)
                res = deque()
                continue
            res.append(br)
            
        string = ""
        for x in result:
            string += "".join(m for m in x)
        return string