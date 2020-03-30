class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #bruteforce
        
        temp = heights[:]
        
        temp.sort()
        count = 0
        for i in range(len(temp)):
            if heights[i] != temp[i]:
                count += 1
        
        return count