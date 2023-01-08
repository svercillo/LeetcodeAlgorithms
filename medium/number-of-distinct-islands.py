class Solution:
    def numDistinctIslands(self, grid) -> int:

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        n = len(grid)
        m = len(grid[0])

        visited = set()

        def dfs(i, j, path, depth, k):
            nonlocal n, m, grid

            if (i, j) in visited:
                return

            visited.add((i, j))

            path.append(f"{depth}:{k}")
            for k, d in enumerate(dirs):
                down, right = d
                ti = i + down
                tj = j + right

                if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 1:
                    dfs(ti, tj, path, depth + 1, k)

        distinct_islands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, 0, -1)

                    # print(path)

                    if path != []:
                        distinct_islands.add(tuple(path))

        return len(distinct_islands)
