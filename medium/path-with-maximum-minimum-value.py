class Solution:
    def maximumMinimumPath(self, grid) -> int:

        n = len(grid)
        m = len(grid[0])

        _max = -1
        for i in range(n):
            for j in range(m):
                _max = max(_max, grid[i][j])

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j, k):
            visited = set()

            def recurse(i, j, k):
                n = len(grid)
                m = len(grid[0])

                nonlocal visited

                if (i, j) in visited:
                    return False

                visited.add((i, j))

                if (i, j) == (n - 1, m - 1):
                    return True

                valid = False
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] >= k:
                        valid = valid or recurse(ti, tj, k)

                return valid

            return recurse(i, j, k)

        l, r = 0, _max + 1

        while l <= r:

            m = (l + r) // 2
            if m <= grid[0][0]:

                last = dfs(0, 0, m)
                curr = dfs(0, 0, m + 1)

                if last and not curr:
                    return m
                elif last and curr:
                    l = m + 1
                elif not last:
                    r = m - 1
            else:
                r = m - 1

        while l >= 0 and not (l <= grid[0][0] and dfs(0, 0, l)):
            l -= 1
        return l
