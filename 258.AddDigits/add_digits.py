class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        
        while len(str_num) != 1:
            result = 0
            for c in str_num:
                result += int(c)
            str_num = str(result)
        
        return int(str_num)