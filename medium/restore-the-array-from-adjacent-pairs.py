class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:

        graph = defaultdict(lambda: set())

        for a, b in pairs:
            graph[a].add(b) 
            graph[b].add(a)

        start_ele = -1
        print(graph)
        for k in graph:
            if len(graph[k]) == 1:
                start_ele = k
        
        visited = set()
        path = []
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            path.append(node)

            for neigh in graph[node]:
                dfs(neigh)

        dfs(start_ele)
        return path
            
