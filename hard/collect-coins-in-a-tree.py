from pprint import pprint
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        graph = {} 
        for a,b in edges:
            if a not in graph:
                graph[a] =set()
            if b not in graph:
                graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)
        q = deque()
        for node in graph:
            if len(graph[node]) == 1:
                if not coins[node]:
                    q.appendleft(node)
                else:
                    q.append(node)
        prunnedleaves = False
        count = 2

        while len(q) and count:
            nq = deque()
            if coins[q[0]]:
                prunnedleaves = True

            if prunnedleaves:
                count -= 1
            
            for i, node in enumerate(q):
                if coins[node] and not prunnedleaves:
                    t = deque(list(q)[i:])

                    for e in nq:
                        if coins[e]:
                            t.append(e)
                        else:
                            t.appendleft(e)
                          
                    nq = t
                    break
                for neigh in graph[node].copy(): 
                    graph[neigh].remove(node)
                    if len(graph[neigh]) == 1:
                        if coins[neigh]:
                            nq.appendleft(neigh)
                        else:
                            nq.append(neigh)
                graph.pop(node)

            q = nq

        return max(0 , (len(graph) - 1) * 2)

        # count steps
        


        
        

