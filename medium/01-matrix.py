import math
class Solution:
    def updateMatrix(self, mat):
        res = []
        inds = set()
        for i in range(len(mat)):
            rows = []
            for j in range(len(mat[0])): 
                if mat[i][j] == 0:
                    inds.add((i, j))
                    rows.append(0)
                else:
                    rows.append(math.inf)     
            res.append(rows)

        dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        w = 0
        while len(inds) > 0:
            newinds = set()

            for i, j in inds:
                res[i][j] = w
            
            for i, j in inds:
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if 0 <= ti < len(mat) and 0 <= tj < len(mat[0]):
                        if res[ti][tj] == math.inf: 
                            print(res[ti][tj])
                            newinds.add((ti,tj))
            inds = newinds
            w += 1
            # break

        return res
            
