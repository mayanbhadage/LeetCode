class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        points = set()
        
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        num = 0
        
        for stone in stones:
            i = stone[0]
            j = stone[1]
            points.add((i,j))
            
            rows[i].append(j)
            cols[j].append(i)
        
        for stone in stones:
            m,n = stone
            if (m,n) in points:
                self.dfs(points, stone[0], stone[1], rows, cols)
                num += 1
        return len(stones) - num
        
        
    def dfs(self, points, x, y, rows, cols):
        points.discard((x,y))
        
        for p in rows[x]:
            if (x,p) in points:
                self.dfs(points, x, p, rows, cols)
        
        for q in cols[y]:
            if (q,y) in points:
                self.dfs(points, q, y, rows, cols)
        