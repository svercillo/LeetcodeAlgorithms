class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
 
        graph = {} 
        first_key = None
        for x, y in edges: 
            first_key = x
            
            if x not in graph: 
                graph[x] = set()
            if y not in graph: 
                graph[y] = set()
                
            graph[x].add(y)
            graph[y].add(x)
        
        if len(edges) != n-1:
            return False
        if len(edges) == 0:
            if n ==1:
                return True  
            else:
                return False
        
        if len(graph) != n:
            return False
        
        cycle = [False]
        
        p_visited = set()
        visited = set()
        def dfs(node, parent):
            p_visited.add(node)

            if node in visited:
                cycle[0] = True
                return
            visited.add(node)
            for conn in graph[node]:
                if conn == parent: # 
                    continue
                
                dfs(conn, node)
            visited.remove(node)
    
        dfs(first_key, None)
        iscycle = cycle[0] 
        visited_all = len(p_visited) == n  # cant be disjoint 
        
        print(iscycle, visited_all)
        
        return not iscycle and visited_all
