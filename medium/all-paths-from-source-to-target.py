class Solution:
    
    def allPathsSourceTarget(self, graph):
        
        n = len(graph)
        res = [] 
        
        def dfs(index, path):
            
            path.append(index)
            
            if index == n-1: 
                res.append(path)
                return
            
            for conn in graph[index]:    
                new_path = [p for p in path]
                dfs(conn, new_path)
    
        dfs(0, [])
        return res
