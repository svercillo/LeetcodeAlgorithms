class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        @cache
        def num_paths(i, j, num_prev_moves):
            nonlocal maxMove, m, n
            if not (0 <= i < m and 0 <= j < n):
                return 1
            
            if num_prev_moves == maxMove:
                return 0

            num_ways = 0
            for down, right in dirs: 
                ti = i + down
                tj = j + right


                num_ways += num_paths(ti, tj, num_prev_moves +1) 

            return num_ways    


        return num_paths(startRow, startColumn, 0) % (10 ** 9 + 7)
