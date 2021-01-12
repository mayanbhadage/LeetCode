class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list)
        self.builtGraph( equations, values)
        print(self.graph)
        result = []
        for query in queries:
            result.append(self.bfs(query))
        return result
    
    def bfs(self, query):
        start, end = query
        visited = set()
        if start not in self.graph and end not in self.graph:
            return -1.0
        
        queue = deque([(start, 1.00)])
        
        while queue:
            curr, prod = queue.popleft()
            visited.add(curr)
            if curr == end:
                return prod
            for n, p in self.graph[curr]:
                if n not in visited:
                    visited.add(n)
                    queue.append((n, prod*p))
        return -1
        
    def builtGraph(self, equations, values):
        for equation, value in zip(equations, values):
            self.graph[equation[0]].append((equation[1], value))
            self.graph[equation[1]].append((equation[0], 1/value))