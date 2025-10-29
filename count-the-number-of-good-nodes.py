class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = {}

        for a, b in edges:
            if a not in graph:
                graph[a] = set()

            if b not in graph:
                graph[b] = set()

            graph[a].add(b)
            graph[b].add(a)

        # make graph directed
        def removeInvalidEdges(node):
            
            for child in graph[node]:
                graph[child].discard(node) # discard the reverse edge
                removeInvalidEdges(child)
            
        removeInvalidEdges(0)


        @cache
        def subtreeSize(node):    
            print(node)
            size = len(graph[node])
            for child in graph[node]:
                size += subtreeSize(child)
                
            return size 


        count = 0
        for root in graph:
            nodes = graph[root]

            if not len(nodes):
                count += 1
                continue

            
            it = iter(nodes)

            node = next(it, None)
            sbtreeSize = subtreeSize(node)
            
            node = next(it, None)
            invalid = False
            while node:
                if subtreeSize(node) != sbtreeSize:
                    invalid = True
                    break
                node = next(it, None)
            

            if not invalid:
                count += 1

        return count
