class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n = len(pid) 
        
        
        graph = {}
        for i in range(n):
            parent = ppid[i] 
            if parent not in graph:
                graph[parent] = []
            if pid[i] not in graph:
                graph[pid[i]] = []
            graph[parent].append(pid[i])
        
        
        if kill not in graph:
            print(graph, kill )
            return []
        
        else:
            removed = []
            
            def dfs(node):
                nonlocal removed
                removed.append(node)
                
                if node in graph:
                    for child in graph[node]:
                        dfs(child)
            
            dfs(kill)
            
            return removed
