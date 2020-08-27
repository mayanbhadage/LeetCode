class Solution:
    def decodeString(self, s: str) -> str:
        currNum = 0
        currStr = ""
        stack = []
        for char in s:
            if char.isdigit():
                currNum = 10 * currNum + int(char)
            elif char == "[":
                stack.append((currStr,currNum))
                currStr = ""
                currNum = 0
                
            elif char == "]":
                prevStr,num = stack.pop()
                currStr = prevStr + currStr * num
                
            else:
                currStr += char
        
        return currStr