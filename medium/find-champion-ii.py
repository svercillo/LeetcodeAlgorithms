class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        
        revGraph = {} 
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = set()

            if b not in revGraph:
                revGraph[b] = set()

            revGraph[b].add(a)
            graph[a].add(b)


        champion = None
        for i in range(n): 
            if i not in revGraph: # possible champion
                if champion is not None:
                    return -1 
                champion = i


        
        if champion is not None:
            return champion
        
        return -1 


        

