class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = address.split(".")
        last = len(temp) -1
        res = ""
        for i , x in enumerate(temp):
            if i != last:
                res += (x + "[.]") 
            else:
                res += x

        return res