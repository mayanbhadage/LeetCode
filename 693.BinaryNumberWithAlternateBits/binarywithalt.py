class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = "{0:b}".format(n)
        for i in range(1,len(binary)):
            if binary[i-1] == "1" and binary[i] != "0":
                return False
            elif(binary[i-1] == "0"and binary[i] != "1"):
                return False
        return True