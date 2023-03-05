class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])

        
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]


        visited = set()

        res = [] 

        remaining_nums = n * m
        cdir = 0 # current direction
        i, j = 0,0
        while remaining_nums:

            res.append(matrix[i][j])
            visited.add((i,j))
            # try current direction 
            ti = i + directions[cdir % 4][0]
            tj = j + directions[cdir % 4][1]

            if not (0 <= ti < n and 0 <= tj < m) or (ti,tj) in visited: # change direction
                cdir += 1
                ti = i + directions[cdir % 4][0]
                tj = j + directions[cdir % 4][1]


            i,j = ti, tj

            remaining_nums -= 1

        return res
