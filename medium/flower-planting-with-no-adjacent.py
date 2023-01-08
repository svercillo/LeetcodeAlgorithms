class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        possible = []
        res = [-1] * (n+1)
        for i in range(n+1):
            possible.append(set([1,2,3,4]))
            
        
        graph = {}
        for x, y in paths: 
            if x not in graph: 
                graph[x] = set()
                
            if y not in graph:
                graph[y] = set()
                
            graph[x].add(y)
            graph[y].add(x)

            
        visited = set()
        
        for k in range(1, n+1):
            q = [k]

            while len(q):
                new_q = []

                for node in q:
                    
                    if node in visited:
                        continue


                    visited.add(node)

                    flower = possible[node].pop()
                    possible[node] = set([flower])

                    if node in graph: 
                        for conn in graph[node]:
                            if flower in possible[conn]:
                                possible[conn].remove(flower)

                            new_q.append(conn)

                q = new_q
            
        return [_set.pop() for i, _set in enumerate(possible) if i > 0 ]
