class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        n, m = len(grid), len(grid[0])

        rows = [0] * m 
        cols = [0] * n
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[j] += 1
                    cols[i] += 1


        for i in range(n):
            for j in range(m):
                grid[i][j] = rows[j] + cols[i] - (m - rows[j] + n - cols[i])


        return grid
        

                
