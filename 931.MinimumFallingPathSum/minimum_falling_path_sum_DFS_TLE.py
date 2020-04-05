class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        result = []
        self.min_val = math.inf
        directions = [(1,-1), (1,0), (1,1)]
        
        for x in range(m):
            
            self.dfs(0, x, 0, directions, m, n, A, result, 1)
        return self.min_val
            
        
            
    def dfs(self,currRow, currCol, currSum, directions, M, N, A, result, count):
        if 0 <= currRow < M and 0 <= currCol < N:
            currSum += A[currRow][currCol]
            if count == N:
                    self.min_val = min(self.min_val, currSum)
                    count = 0
                    return

            for direction in directions:
                newRow = currRow + direction[0]
                newCol = currCol + direction[1]
                self.dfs(newRow, newCol, currSum, directions, M, N, A, result,count + 1)

            
                