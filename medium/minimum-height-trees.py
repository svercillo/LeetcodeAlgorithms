class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = dict()
        for a, b in edges:
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()

            graph[a].add(b)
            graph[b].add(a)


        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)


        while len(graph) > 2:
            nleaves = set()
            for leaf in leaves:
                if leaf not in graph or not len(graph[leaf]):
                    continue
            
                friends = graph[leaf]

                assert len(friends) == 1

                parent = [e for e in friends][0]
                if leaf in graph[parent]:
                    graph[parent].remove(leaf)

                    if len(graph[parent]) <=1:
                        nleaves.add(parent)

                graph.pop(leaf)
            leaves = nleaves

        
        return [node for node in graph]
                
                
            


