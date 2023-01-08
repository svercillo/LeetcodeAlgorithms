class Solution:
    def calcEquation(self, equations, values, queries):

        graph = {}

        for i, eq in enumerate(equations):
            a, b = eq

            if a not in graph:
                graph[a] = {}

            if b not in graph:
                graph[b] = {}

            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        # print(graph)

        resarr = []

        for a, b in queries:
            arrived = False

            def dfs(product, node, target, visited):
                # print(node, target, graph[node])
                nonlocal arrived
                if node in visited or arrived:
                    return 1
                visited.add(node)

                if node not in graph or target not in graph:
                    return 1

                if target in graph[node]:
                    arrived = True
                    return product * graph[node][target]
                else:

                    res = 1
                    for a2 in graph[node]:
                        res *= dfs(product * graph[node][a2], a2, target, visited)

                    return res

            result = dfs(1, a, b, set())
            resarr.append(result if arrived else -1)

        return resarr

