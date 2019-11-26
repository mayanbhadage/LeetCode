class Solution:
    def tribonacci(self, n: int) -> int:
        hmap = {0:0,1:1,2:1}
        
        for i in range(3,38):
            hmap[i] = hmap[i-1] + hmap[i-2] + hmap[i-3]
        return hmap[n]