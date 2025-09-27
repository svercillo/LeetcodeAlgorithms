import math
class Solution:
    def highestPeak(self, isWater):
        n, m = len(isWater), len(isWater[0])

        res = []
        inds = set()
        for i in range(n):
            row = []
            for j in range(m):
                if isWater[i][j]:
                    inds.add((i,j))
                    row.append(0)    
                else: 
                    row.append(math.inf)
            res.append(row)


        dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        h = 0
        while len(inds):
            newinds = set()
            
            for i, j in inds:

                for down, right in dirs:
                    ti = i + down 
                    tj = j + right

                    if 0 <= ti < n and 0 <= tj < m:

                        if res[ti][tj] == math.inf:
                            
                            res[ti][tj] = h + 1

                            newinds.add((ti, tj))

            inds = newinds
            h += 1

        return res

            
