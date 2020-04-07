class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        pointsA = []
        pointsB = []
        
        rows = len(A)
        cols = len(A[0])
        
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1:
                    pointsA.append((row,col))
                if B[row][col] == 1:
                    pointsB.append((row,col))   
                    
                    
        
        ans = 0
        dic = collections.defaultdict(int)
        
        for pointA in pointsA:
            for pointB in pointsB:
                rel_pos = (pointA[0] - pointB[0]) ,(pointA[1] - pointB[1])
                dic[rel_pos] += 1
                ans = max(ans, dic[rel_pos])
        print (dic)
        return ans
        