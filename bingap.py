class Solution:
    def binaryGap(self, N: int) -> int:
        binary = "{0:b}".format(N)
        
        length = len(binary)
        max_dist = 0
        for i in range(0,length):
            if(binary[i] == "1"):
                for j in range(i+1, length):
                    if binary[j] == "1":
                        if j-i > max_dist:
                            max_dist = j-i
                            break;
                        break;
        return max_dist