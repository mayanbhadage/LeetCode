class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        #BruteForce O(N * M)
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] < 0:
                    count += 1
        return count