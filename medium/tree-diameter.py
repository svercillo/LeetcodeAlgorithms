class Solution:
    def treeDiameter(self, edges) -> int:

        
        if edges == []:
            return 0
        graph = {}

        for p, c in edges:
            if p not in graph:
                graph[p] = set()

            if c not in graph:
                graph[c] = set()

            graph[p].add(c)
            graph[c].add(p)

        curr_path = set()

        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node in curr_path:
                return 0
            
            longest = 0
            secondlongest = 0
            curr_path.add(node)
            for child in graph[node]:
                childsum = dfs(child)
                
                if childsum > longest:
                    secondlongest = longest
                    longest = childsum 
                elif childsum > secondlongest: 
                    secondlongest = childsum
            curr_path.remove(node)
            
            diameter = max(longest + secondlongest, diameter)
            
            return longest + 1

        
        start_node = next(iter(graph))
        dfs(start_node)
        
        
        return diameter
