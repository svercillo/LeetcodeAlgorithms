class Solution:
    def minReorder(self, n: int, connections) -> int:
        directed = {}
        undirected = {}
        res = [0]

        for a, b in connections:
            if a not in directed:
                directed[a] = set()
            directed[a].add(b)

            if a not in undirected:
                undirected[a] = set()
            undirected[a].add(b)

            if b not in undirected:
                undirected[b] = set()
            undirected[b].add(a)

        visited = set()

        def dfs(node):

            if node in visited:
                return

            print(node)
            visited.add(node)

            for conn in undirected[node]:
                if conn not in visited:
                    valid = False
                    if conn in directed:
                        if node in directed[conn]:
                            valid = True

                    if not valid:
                        print(node, directed)
                        print(node, conn)
                        res[0] += 1

                dfs(conn)

        dfs(0)

        return res[0]


res = Solution().minReorder(n=3, connections=[[1, 0], [2, 0]])
print(res)
