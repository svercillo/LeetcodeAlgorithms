from typing import List
import math
from pprint import pprint
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def rotate90(grid):
            n, m = len(grid), len(grid[0])
            ngrid = []
            for j in range(m):
                row = []
                for i in range(n-1, -1, -1):
                    row.append(grid[i][j])

                ngrid.append(row)
            return ngrid 

        def calcslices(grid):
            # print(f"grid {grid}")
            n, m = len(grid), len(grid[0])
            res = math.inf
            for i in range(1, n-1):
                # print("calc slices ")
                for j in range(i+1, n):
                    # print("other")
                    total = minarea(grid, 0, i, 0, m)
                    total += minarea(grid, i, j, 0, m)
                    total += minarea(grid, j, n, 0, m)
                    res = min(abs(total), res)
            
            return res

        def calcdropping(grid):
            n, m = len(grid), len(grid[0])

            res = math.inf
            for i in range(1, n):
                # print("calc slices ")

                for t in range(1,m):
                    # print("other")

                    total = minarea(grid, 0, i, 0, m)
                    total += minarea(grid, i, n, 0, t)
                    total += minarea(grid, i, n, t, m)

                    res = min(res, abs(total))
            
            # print(res)
            return res

        def calcrising(grid):
            n, m = len(grid), len(grid[0])

            res = math.inf
            for i in range(n-1-1, 0, -1):
                # print("calc slices ")

                for t in range(1,m):
                    # print("other")
                    total = minarea(grid, i, n, 0, m)
                    total += minarea(grid, 0, i, 0, t)
                    total += minarea(grid, 0, i, t, m)        

                    res = min(res, abs(total))
            return res 


        def pgrid(grid, i1, i2, j1, j2):
            mat = []
            for i in range(i1, i2):
                row = []
                for j in range(j1, j2) :
                    row.append(grid[i][j])
                mat.append(row)
            # pprint(mat)


        def minarea(grid, i1, i2, j1, j2):
            
            istart, iend = -1, -1
            jstart, jend = math.inf, -math.inf
            for i in range(i1, i2):
                start, end = -1, -1
                for j in range(j1, j2):
                    if grid[i][j] == 1:
                        iend = i
                        if istart == -1:
                            istart = i

                        end = j
                        if start == -1:
                            start = j
                
                if start != -1:
                    jstart = min(start, jstart)
                    jend = max(end, jend)

            if math.inf in [iend, istart, jend, jstart]:
                pgrid(grid, i1, i2, j1, j2) 
                # print("VALUE", 0)
                return 0 
            
            
            pgrid(grid, i1, i2, j1, j2)
            # print("VALUE", (iend - istart+ 1) * (jend - jstart + 1) )
            return (iend - istart+ 1) * (jend - jstart + 1) 
            

        return min(
            calcrising(grid),
            calcrising(rotate90(grid)),
            calcslices(grid),
            calcslices(rotate90(grid)),
            calcdropping(grid),
            calcdropping(rotate90(grid))
        )
                

res = Solution().minimumSum(
    [[0,0,0,0],[0,1,0,0],[1,0,1,0]]
)

print(res)
