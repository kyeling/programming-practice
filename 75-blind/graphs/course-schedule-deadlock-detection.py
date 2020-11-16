class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]  # make into dir graph, idx = node, corresponding list is neighbors
        visited = [0 for _ in range(numCourses)]
        
        # Create the directed graph
        for pair in prerequisites:
            i, j = pair
            graph[i].append(j)
            
        for i in range(numCourses):
            # when dfs ends prematurely, we found a cycle
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 1
        return True
        
# deadlock (term used in distributed systems): 
#     resources all dependent on each other, can't get any done
# cycle (in graphs): can use topological sort but in this case use deadlock detection (dfs to find cycle)
#     array of all 0, visted if -1
# time: O(n), space: O(e) where e =  # of edges
        
