import heapq
import math

class Solution:

    class Vertex:
        def __init__(self, index, cost):
            self.index = index
            self.cost = cost 
            self.visited = False
            self.duplicate = False
        
        def __lt__(self, other):
            return self.cost < other.cost

        def __repr__(self):
            return f"Node<{self.index}, {self.cost}, {self.visited}, {self.duplicate}>"

    def minCost(self, n: int, edges) -> int:
        graph = {}         
        for u, v, w in edges:
            if u not in graph: 
                graph[u] = {}

            if v not in graph:
                graph[v] = {}

            if v not in graph[u]:
                graph[u][v] = math.inf
            
            if u not in graph[v]:
                graph[v][u] = math.inf

            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(2 * w, graph[v][u]) 

        for i in range(n):
            if i not in graph:
                graph[i] = {}

        # print(graph)
        vMap = {
            i : self.Vertex(i, math.inf) for i in range(n)
        }

        vOrder = [vMap[ind] for ind in vMap]
        vMap[0].cost = 0
        vMap[0].visited = True

        heapq.heapify(vOrder)

        while len(vOrder):
            # print(vOrder)
            topNode = heapq.heappop(vOrder)
            if topNode.duplicate:
                # remove tombstones
                continue

            if topNode.cost == math.inf:
                break

            if topNode.index == n -1: 
                return topNode.cost

            topNode.visited = True

            for v in graph[topNode.index]:
                vNode = vMap[v]
                if vNode.visited:
                    continue

                tCost = graph[topNode.index][v]                
                vNode.duplicate = True
                
                newVNode = self.Vertex(vNode.index, min(vNode.cost, topNode.cost + tCost))
                vMap[v] = newVNode
                heapq.heappush(vOrder, newVNode)

        return -1
