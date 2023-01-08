class Solution:
    def knightDialer(self, p: int) -> int:
        grid = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [-1, 0, -1]
        ]
        directions = [
            [-1, -2,], [-2, -1], [-2, 1],[-1, 2], [1, 2], [2, 1], [2, -1], [1,-2]
        ]
        n, m = 4, 3

        def get_storage():
            arr = []
            for i in range(n):
                row = []
                for j in range(m):
                    row.append(0)
                arr.append(row)

            return arr

        dp = get_storage()

        first_sum = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    continue
                
                for down, right in directions:
                    ti, tj = i + down, j + right

                    if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] != -1:
                        dp[i][j] += 1

        if p == 1: 
            return 10



        total_count = 0
        for k in range(1, p-1):
            next_dp = get_storage()
            for i in range(n):
                for j in range(m):

                    if grid[i][j] == -1: 
                        continue
                    
                    for down, right in directions:
                        ti, tj = i + down, j + right

                        if (
                            0 <= ti < n 
                            and 0 <= tj < m 
                            and grid[ti][tj] != -1
                        ):
                            next_dp[i][j] += dp[ti][tj]
            dp = next_dp
                    

        return sum([sum(row) for row in dp]) % (10 ** 9 + 7)

