class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid) , len(grid[0] )


        dirs = [
            [1, 1], # top left -> bottom right
            [1, -1], # top right -> bottom left
            [-1,-1], # bottom right -> top left      => 4
            [-1, 1] # bottom left -> top right
        ]

        def inrange(i, j):
            return 0<= i < n and 0<= j < m

        # dp[i][j][d] = (length, isStart) or None
        dp = [[[None] * 4 for _ in range(m)] for _ in range(n)]

        def longest(i, j, dind):
            """Manual memoization replacement for @cache."""
            if dp[i][j][dind] is not None:
                return dp[i][j][dind]

            down, right = dirs[dind]

            if grid[i][j] == 1:
                # parent direction = backwards diagonal
                pi = i - down
                pj = j - right
                if inrange(pi, pj) and grid[pi][pj] == 2:
                    dp[i][j][dind] = (0, True)
                else:
                    dp[i][j][dind] = (0, False)
                return dp[i][j][dind]

            v = grid[i][j]
            ti = i + down
            tj = j + right

            if (
                inrange(ti, tj)
                and grid[ti][tj] in {v ^ 2, 1}  # your original logic
            ):
                l, isstart = longest(ti, tj, dind)
                dp[i][j][dind] = (l + 1, isstart)
            else:
                dp[i][j][dind] = (1, False)

            return dp[i][j][dind]
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: # 1 can't be inflection point
                    res = max(res ,1)
                    continue

                for d in range(4):
                    dind = (d + 2) % 4 # flip the arrow
                    ndind = (d + 1) % 4 # 90 degrees 

                    l1, iss1 = longest(i, j, dind)
                    l2, iss2 = longest(i, j, ndind)

                    lt = l1 + l2 + 1
                    if l1 and l2:
                        lt -=1  # remove overlapped square

                    if not iss1:
                        continue
                    res = max(res, lt)

        return res
                            

                
