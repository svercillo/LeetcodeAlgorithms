class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        
        graph = []
        for _ in range(n):
            graph.append(set())
    
        for a, b in enumerate(edges):
            if a != b: 
                graph[a].add(b)
            else:
                graph[a] = set()

        @cache
        def maxCycleLen(node): 
            nonlocal count

            # print(node, seen)
            if node in seen:
                # print("HERE", count)
                return count - seen[node]
            
            seen[node] = count
            count += 1
            mlength = -1
            # print(node)
            for neigh in graph[node]:
                if neigh == -1:
                    continue
                size = maxCycleLen(neigh)
                mlength = max(mlength, size)
            count -= 1
            seen.pop(node)

            return mlength 


        # print("N", n, graph)
        mlength = -1
        for node in range(n):
            # print("nod ", node)
            seen = {} # node and the iteration it was inserted at
            count = 0
            mlength = max(mlength, maxCycleLen(node))

        return mlength
        



