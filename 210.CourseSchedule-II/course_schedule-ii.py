class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or len(prerequisites) == 0:
            return True
        
        
        #Initilize the graph and in_degree
        graph = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        
        
        #Built the graph and indegree
        for edge in prerequisites:
            parent = edge[0]
            child = edge[1]
            graph[parent].append(child)
            indegree[child] += 1
        
        
        sources = deque()
        #Find the sources(with indegree 0)
        
        for key, value in indegree.items():
            if value == 0:
                sources.append(key)
                
        #TopoSort
        sortedGraph = []
        while sources:
            curr_vertex = sources.popleft()
            sortedGraph.append(curr_vertex)
            for child in graph[curr_vertex]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)
                    
        
        
        if len(sortedGraph) != numCourses:
            return False
        else:
            return True
        
        
        
        
        
        