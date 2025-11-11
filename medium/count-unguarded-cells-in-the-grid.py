from pprint import pprint
class Solution:
    def countUnguarded(self, n, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        free = [] 
        for i in range(n):
            free.append([1] * m)

        dirs = [
            [0,1],
            [0,-1],
            [1, 0 ],
            [-1, 0]
        ]
        
        q = []
        blocked = set()
        for coords in guards:
            i, j = coords
            blocked.add(tuple(coords))

            for d in dirs:
                q.append((coords, d))

        for coords in walls:
            blocked.add(tuple(coords))

        

        while len(q):

            pprint(q)
            nq = []
            for coords, d in q:
                i, j = coords

                free[i][j] = 0

                ti = i + d[0]
                tj = j + d[1]

                if not (0<= ti < n and 0<= tj < m) or (ti,tj) in blocked:
                    continue

                nq.append(((ti, tj), d))


            q = nq


        for i, j in blocked:
            free[i][j] = 0

        return sum([sum(row) for row in free])
            

        



        


        



        
        
