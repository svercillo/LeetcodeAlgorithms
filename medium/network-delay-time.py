class Solution:
    def networkDelayTime(self, edges: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(dict)
        for a, b, w in edges:
            graph[a][b] = w

        # dijstras but don't stop
        nodews = {i:math.inf for i in range(1, n+1)}
        nodews[k] = 0

        q = [(0, k)]
        visited = set()
        while len(q):
            print(q)
            topw, top = heapq.heappop(q)
            if top in visited:
                continue
            visited.add(top)

            for neigh in graph[top]:
                w = graph[top][neigh]

                if topw + w < nodews[neigh]:
                    nodews[neigh] = topw + w
                    heapq.heappush(q, (topw + w, neigh))

        if len(visited) < n:
            return -1


    
        return max([nodews[e] for e in nodews])

            




        
                

                
        





        


