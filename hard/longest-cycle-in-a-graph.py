class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = {}
        reverse_graph = {}
        for i, outgoing in enumerate(edges):
            if i not in graph:
                graph[i] = set()

            if outgoing != -1:
                graph[i].add(outgoing)


            if outgoing not in reverse_graph:
                reverse_graph[outgoing] = set()

            if outgoing != -1:
                reverse_graph[outgoing].add(outgoing)


        path = {}
        longest_cycle_len = -1


        print(graph)
        print(reverse_graph)
        starting_nodes = []

        for i in range(n):
            if i not in reverse_graph or len(reverse_graph) == 0:
                starting_nodes.append(i)



        visited = set()
        # @cache
        def dfs(node, depth):
            nonlocal longest_cycle_len

            
            if node in path:
                cycle_len = depth - path[node]
                longest_cycle_len = max(cycle_len, longest_cycle_len)
                return

            
            if node in visited:
                return
            
            visited.add(node)


            path[node] = depth
            for v in graph[node]:
                dfs(v, depth + 1)

            path.pop(node)


        # for i in starting_nodes:
        #     dfs(i, 0)
        for i in range(n):
            dfs(i, 0)


        return longest_cycle_len
        

