class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # Generate Adj List
        n = len(M)
        graph = {}
        # init graph
        for i in range(n):
            graph[i] = set()

        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                count += 1
        return count

    def dfs(self,graph, idx, visited):
        visited.add(idx)
        for n in graph[idx]:
            if n not in visited:
                self.dfs(graph, n, visited)