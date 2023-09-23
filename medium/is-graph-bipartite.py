class Solution:
    def isBipartite(self, adjList: List[List[int]]) -> bool:

        graph = {}
        for u, row in enumerate(adjList):
            for v in row:
                if u not in graph:
                    graph[u] = set()

                graph[u].add(v)

                if v not in graph:
                    graph[v] = set()

                graph[v].add(u)


        partitions = {}

        def assignPartition(node, isA, firstCheck):

            if node in partitions:
                if firstCheck:
                    return True
                else:
                    print("HERE", partitions[node] == isA)
                    return partitions[node] == isA

            
            valid = True
            partitions[node] = isA
            for neigh in graph[node]:
                if not assignPartition(neigh, not isA, False):
                    return False

            return True

        
        valid = True
        # check all the connected components
        for node in graph:
            if not assignPartition(node, True, True):
                valid = False

        return valid
            

