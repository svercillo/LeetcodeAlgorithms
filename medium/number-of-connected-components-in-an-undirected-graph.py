class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        for edge in edges:
            a, b = edge

            if a not in graph:
                graph[a] = set()

            if b not in graph:
                graph[b] = set()

            graph[a].add(b)
            graph[b].add(a)

        visited = set()
        seen = set()

        def dfs(num):

            if num in seen or num in visited:
                return  # indicates cycle

            visited.add(num)

            seen.add(num)

            # print(graph[num])
            for connected in graph[num]:
                dfs(connected)

            seen.remove(num)

        components_count = 0
        for i in range(n):
            if i in graph:
                if i not in visited:
                    dfs(i)
                    components_count += 1
            else:
                components_count += 1

        return components_count
