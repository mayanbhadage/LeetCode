class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #Brute Force Approach
        result = []
        for i in range(0,len(T)):
            for j in range(i,len(T)):
                
                if T[j] > T[i]:
                    result.append(j-i)
                    break
                
                if j == len(T)-1:
                    result.append(0)
        return result