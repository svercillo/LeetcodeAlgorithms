class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)

        for a, neigh in enumerate(isConnected):
            for b, valid in enumerate(neigh): 
                if valid: 
                    graph[b].add(a)

                    graph[a].add(b)

        # union find
        parentmapping = [-1]  * n
        def dfs(node, parent):
            if parentmapping[node] != -1:
                return

            parentmapping[node] = parent
            for neigh in graph[node]:
                dfs(neigh, parent)

        for node in range(n):
            dfs(node, node)
                
        return len(set(parentmapping))
            
                
                

                


        
