import heapq
import math
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        def creategraph():
            graph = {}
            for x, y, w in flights:
                if x not in graph:
                    graph[x] = {}

                graph[x][y] = w

            for i in range(n):
                if i not in graph:
                    graph[i] = {}
            return graph

        graph = creategraph()
        q = [(-1,0, src)] # stops, cost, node 
        

        seen = [-9999999] * n
        res = [math.inf] * n

        while len(q):
            # print(q, seen)
            stops, cost, node = heapq.heappop(q)


            if stops > k or seen[node] == stops: 
                continue
            seen[node] = stops

            res[node] = min(cost, res[node ])

            for ynode in graph[node]:
                new_cost = graph[node][ynode] + cost
                new_stops = stops + 1

                heapq.heappush(q, (new_stops, new_cost, ynode))


        print(res)
        return res[dst] if res[dst] != math.inf else -1


















        
            


        
