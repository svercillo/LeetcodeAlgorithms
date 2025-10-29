class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = defaultdict(dict)

        edgews = set([0])
        for a, b, w in edges:
            graph[a][b] = w
            graph[b][a] = w
            edgews.add(w)
        edgews = sorted(list(edgews))
        

        # if we can make k connected components with les than min
        def condition(minweightind):
            # print(minweightind)
            minweight = edgews[minweightind]
            pmapping = [-1] * n

            def dfs(node, parent): 
                if pmapping[node] != -1:
                    return
                pmapping[node] = parent
                for neigh in graph[node]:
                    w = graph[node][neigh]
                    # print(graph[node][neigh], minweight)
                    if w <= minweight: 
                        dfs(neigh, parent)
            
            for node in range(n):
                dfs(node, node)

            # print(pmapping)

            return len(set(pmapping)) <= k
            
        # print(edgews)
        l, r = 0, len(edgews) -1 
        while l < r:
            m = (l+r)// 2
            # print(l, r)
            if condition(m):
                r = m
            else:
                l = m + 1


        # print(condition(0), edgews[0])
        # print(condition(1), edgews[1])
        # print(condition(2), edgews[2])
        # print(condition(3), edgews[3])


        return edgews[l]





