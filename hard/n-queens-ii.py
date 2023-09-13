class Solution:
    def totalNQueens(self, n: int) -> int:

        r_used = set()
        d_diag = set()
        u_diag = set()


        def dfs(col):
            nonlocal n
            if col == n:
                return 1

            num_ways = 0

            for row in range(n):
                if (
                    row not in r_used 
                    and row - col not in d_diag 
                    and row + col not in u_diag
                ):

                    r_used.add(row)
                    d_diag.add(row-col)
                    u_diag.add(row + col)
                    
                    
                    num_ways += dfs(col + 1)

                    r_used.remove(row)
                    d_diag.remove(row-col)
                    u_diag.remove(row + col)

            return num_ways

        return dfs(0)
