from pprint import pprint


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines) -> int:
        m = n

        grid = [[1] * n for _ in range(n)]
        for x,y in mines:
            grid[x][y] = 0
        

        dp = [[0, 0] * m for _ in range(n)]

        dp_fw = []
        dp_bw = []

        print(grid)

        for i in range(n):
            row1 = []
            row2 = []
            for j in range(m):
                row1.append([0, 0])
                row2.append([0,0])
            dp_fw.append(row1)
            dp_bw.append(row2)

                
        if len(mines) >= n*n:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if i - 1 >= 0:
                    dp_fw[i][j][0] = dp_fw[i-1][j][0] + 1
                else:
                    dp_fw[i][j][0] = 1

                if j -1 >= 0:
                    dp_fw[i][j][1] = dp_fw[i][j-1][1] + 1
                else:
                    dp_fw[i][j][1] = 1



        largest = 1
        for i in range(n -1, -1, -1):
            for j in range(m-1, -1, -1):
                if grid[i][j] == 0:
                    continue
                
                if i + 1 <n:
                    dp_bw[i][j][0] = dp_bw[i+1][j][0] + 1
                else:
                    dp_bw[i][j][0] = 1
                
                if j + 1 < m :
                    dp_bw[i][j][1] = dp_bw[i][j+1][1] + 1
                else:
                    dp_bw[i][j][1] = 1

                dp[i][j] = min([dp_fw[i][j][0], dp_bw[i][j][0], dp_fw[i][j][1], dp_bw[i][j][1]])
                largest = max(largest, dp[i][j])


        return largest
