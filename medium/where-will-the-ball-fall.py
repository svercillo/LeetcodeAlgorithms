class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        def gets_to_bottom(i, j):
            if i == n:
                return j
            if j == m -1 and grid[i][j] == 1:
                return -1
            elif j == 0 and grid[i][j] == -1:
                return -1 
            elif grid[i][j] == 1 and grid[i][j+1] == -1:
                return -1
            elif grid[i][j] == -1 and grid[i][j-1] == 1:
                return -1

            next_j = j +1 if grid[i][j] == 1 else j -1
            return gets_to_bottom(i+1, next_j)


        res = []
        for j in range(m):
            end_col = gets_to_bottom(0, j)
            res.append(end_col)



        return res
